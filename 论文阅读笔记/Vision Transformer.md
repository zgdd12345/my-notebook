# 1.Introduction


# 2.Patch Embeding
标准transformer 接受一维标记嵌入序列（Sequence of token embeddings）作为输入。

**具体操作：**

1. 将图像![image](https://cdn.nlark.com/yuque/__latex/f2748ddbc524c5be858a8ba521b580fa.svg), reshape为一个展平的2D块序列![image](https://cdn.nlark.com/yuque/__latex/3a8f6f31a3d4649cff7d7ba39fcb9ea7.svg)。P是图像块分辨率,![image](https://cdn.nlark.com/yuque/__latex/b59db15bd692892864a3a04d6da6c930.svg)是产生的图像块数，也就是Transformer的有效输入序列长度。
2. Transformer所有层中使用恒定的隐向量（latent vector）大小为D,因此我们将图像块展平，并使用FC层![image](https://cdn.nlark.com/yuque/__latex/e4640420056063c12994c9a93ca61660.svg)将维度![image](https://cdn.nlark.com/yuque/__latex/46c9e22dabb583c6d9764d0b972733c7.svg)映射为D维，得到![image](https://cdn.nlark.com/yuque/__latex/a2e3f5fa48d1ab9a736df8a0b54a495f.svg)。同时保持图块数N不变。

**代码：**

```python
class PatchEmbed(nn.Module):
    """ Image to Patch Embedding """

    def __init__(self, img_size=224, patch_size=16, in_chans=3, embed_dim=768):
        super().__init__()
        img_size = to_2tuple(img_size)  # (H, W)
        patch_size = to_2tuple(patch_size)  # (P, P)
        # N = (H // P) * (W // P)  
        num_patches = (img_size[1] // patch_size[1]) * (img_size[0] // patch_size[0])

        self.img_size = img_size
        self.patch_size = patch_size
        self.num_patches = num_patches

        # 可训练的线性投影 - 获取输入嵌入
        self.proj = nn.Conv2d(in_chans, embed_dim, kernel_size=patch_size, stride=patch_size)

    def forward(self, x):
        B, C, H, W = x.shape
        # FIXME look at relaxing size constraints

        assert H == self.img_size[0] and W == self.img_size[1], \
        f"Input image size ({H}*{W}) doesn't match model (
        {self.img_size[0]}*{self.img_size[1]})."

        # (B, C, H, W) -> (B, D, (H//P), (W//P)) -> (B, D, N) -> (B, N, D)
        #   D=embed_dim=768, N=num_patches=(H//P)*(W//P)
        #   torch.flatten(input, start_dim=0, end_dim=-1)  # 形参：展平的起始维度和结束维度    
        # 可见 Patch Embedding 操作 3 步到位
        x = self.proj(x).flatten(2).transpose(1, 2)
        return x
```

# 3. Learnable Embedding
不重要的操作，可有可无。

# 4. Position Embeddings
Transformer 使用PE保留输入patch之间的位置信息。由于**自注意力的扰动不变性(Permutation-invariant),**既打乱Sequence中的tokens的顺序不会影响结果。

<font style="color:rgb(77, 77, 77);">若不给模型提供图像块的位置信息，那么模型就需要通过patch的语义来学习拼图，这就额外增加了学习成本。ViT 论文中对比了几种不同的位置编码方案：</font>

:::tips
1. <font style="color:rgb(51, 51, 51);">无</font><font style="color:rgb(73, 73, 73);">位置嵌入</font>
2. <font style="color:rgb(51, 51, 51);">1-D</font><font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(73, 73, 73);">位置嵌入</font><font style="color:rgb(51, 51, 51);">：考虑把 2-D 图像块视为 1-D 序列</font>
3. <font style="color:rgb(51, 51, 51);">2-D</font><font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(73, 73, 73);">位置嵌入</font><font style="color:rgb(51, 51, 51);">：考虑图像块的 2-D 位置 (x, y)</font>
4. <font style="color:rgb(51, 51, 51);">相对位置嵌入：考虑图像块的相对位置</font>

:::

**代码：**

```python
# 多 +1 是为了加入上述的 class token
# embed_dim 即 patch embed_dim
self.pos_embed = nn.Parameter(torch.zeros(1, num_patches + 1, embed_dim)) 
 
# patch emded + pos_embed ：图像块嵌入 + 位置嵌入
x = x + self.pos_embed
```

# 5.Transformer encoder
Transformer 编码器由交替的多头注意力层（MSA）和多层感知机块组成（MLP），在每一块前用Layer Norm，每个块后用残差连接。

![整体前向计算过程](https://cdn.nlark.com/yuque/0/2022/png/29307286/1664354338123-f35839b3-48fc-4a6a-ae4f-416b37938bfb.png)

```python
class Attention(nn.Module):
    def init(self, dim, num_heads=8, qkv_bias=False, qk_scale=None, attn_drop=0., proj_drop=0.):
        super().init()
        self.num_heads = num_heads
    	head_dim = dim // num_heads

        self.scale = qk_scale or head_dim ** -0.5
        
        self.qkv = nn.Linear(dim, dim * 3, bias=qkv_bias)
        self.attn_drop = nn.Dropout(attn_drop)
        self.proj = nn.Linear(dim, dim)
        
        # 附带 dropout
        self.proj_drop = nn.Dropout(proj_drop)

    def forward(self, x):
        B, N, C = x.shape
        qkv = self.qkv(x).reshape(B, N, 3, self.num_heads, C // self.num_heads).permute(2, 0, 3, 1, 4)
        q, k, v = qkv[0], qkv[1], qkv[2]  # make torchscript happy (cannot use tensor as tuple)
    
        attn = (q @ k.transpose(-2, -1)) * self.scale
        attn = attn.softmax(dim=-1)
        attn = self.attn_drop(attn)
    
        x = (attn @ v).transpose(1, 2).reshape(B, N, C)
        x = self.proj(x)
        x = self.proj_drop(x)
    
        return x
```

在 Transformer中，MSA 后跟一个 FFN (Feed-forward network)，其包含 两个 FC 层，第一个 FC 将特征从维度D变换成4D，第二个 FC 将特征从维度4D恢复成D ，中间的非线性激活函数均采用 GeLU (Gaussian Error Linear Unit，高斯误差线性单元) —— 这实质是一个 MLP (多层感知机与线性模型类似，区别在于 MLP 相对于 FC 层数增加且引入了非线性激活函数，例如 FC + GeLU + FC)，实现如下：

```python
class Mlp(nn.Module):
    def __init__(self, in_features, hidden_features=None, out_features=None, act_layer=nn.GELU, drop=0.):
        super().__init__()
 
        out_features = out_features or in_features
        hidden_features = hidden_features or in_features
        self.fc1 = nn.Linear(in_features, hidden_features)
        self.act = act_layer()
        self.fc2 = nn.Linear(hidden_features, out_features)
        self.drop = nn.Dropout(drop)
 
    def forward(self, x):
        x = self.fc1(x)
        x = self.act(x)
        x = self.drop(x)
        x = self.fc2(x)
        x = self.drop(x)
 
        return x
```

<font style="color:rgb(77, 77, 77);"> 一个 </font>**<font style="color:rgb(230, 178, 35);">Transformer Encoder Block</font>**<font style="color:rgb(230, 178, 35);"> </font><font style="color:rgb(77, 77, 77);">就包含一个 </font>**<font style="color:rgb(77, 77, 77);">MSA</font>**<font style="color:rgb(77, 77, 77);"> 和一个</font>**<font style="color:rgb(77, 77, 77);"> FFN</font>**<font style="color:rgb(77, 77, 77);">，二者都有 </font>**<font style="color:rgb(77, 77, 77);">跳跃连接 </font>**<font style="color:rgb(77, 77, 77);">和 </font>**<font style="color:rgb(77, 77, 77);">层归一化 </font>**<font style="color:rgb(77, 77, 77);">操作构成 </font>**<font style="color:rgb(156, 142, 193);">MSA Block</font>****<font style="color:rgb(77, 77, 77);"> </font>**<font style="color:rgb(77, 77, 77);">和 </font>**<font style="color:rgb(110, 170, 215);">MLP Block</font>**<font style="color:rgb(77, 77, 77);">，实现如下： </font>

```python
# Transformer Encoder Block
class Block(nn.Module):
    def __init__(self, dim, num_heads, mlp_ratio=4., qkv_bias=False, qk_scale=None, drop=0., attn_drop=0.,
                 drop_path=0., act_layer=nn.GELU, norm_layer=nn.LayerNorm):
        super().__init__()
 
        # 后接于 MHA 的 Layer Norm
        self.norm1 = norm_layer(dim)
        # MHA
        self.attn = Attention(dim, num_heads=num_heads, qkv_bias=qkv_bias, 
                              qk_scale=qk_scale, attn_drop=attn_drop, proj_drop=drop)
        # NOTE: drop path for stochastic depth, we shall see if this is better than dropout here
        self.drop_path = DropPath(drop_path) if drop_path > 0. else nn.Identity()
 
        # 后接于 MLP 的 Layer Norm
        self.norm2 = norm_layer(dim)
        # 隐藏层维度
        mlp_hidden_dim = int(dim * mlp_ratio)
        # MLP
        self.mlp = Mlp(in_features=dim, hidden_features=mlp_hidden_dim, act_layer=act_layer, drop=drop)
 
    def forward(self, x):
        # MHA + Add & Layer Norm
        x = x + self.drop_path(self.attn(self.norm1(x)))
        # MLP + Add & Layer Norm
        x = x + self.drop_path(self.mlp(self.norm2(x)))
        return x
```

**另一种实现：**

```python
# 导入相关模块
import torch
from torch import nn, einsum
import torch.nn.functional as F
from einops import rearrange, repeat
from einops.layers.torch import Rearrange

# 辅助函数，生成元组
def pair(t):
    return t if isinstance(t, tuple) else (t, t)

# 规范化层的类封装
class PreNorm(nn.Module):
    def __init__(self, dim, fn):
        super().__init__()
        self.norm = nn.LayerNorm(dim)
        self.fn = fn
    def forward(self, x, **kwargs):
        return self.fn(self.norm(x), **kwargs)
        
# FFN
class FeedForward(nn.Module):
    def __init__(self, dim, hidden_dim, dropout = 0.):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, dim),
            nn.Dropout(dropout)
        )
    def forward(self, x):
        return self.net(x)
# Attention
class Attention(nn.Module):
    def __init__(self, dim, heads = 8, dim_head = 64, dropout = 0.):
        super().__init__()
        inner_dim = dim_head *  heads
        project_out = not (heads == 1 and dim_head == dim)

        self.heads = heads
        self.scale = dim_head ** -0.5

        self.attend = nn.Softmax(dim = -1)
        self.to_qkv = nn.Linear(dim, inner_dim * 3, bias = False)

        self.to_out = nn.Sequential(
            nn.Linear(inner_dim, dim),
            nn.Dropout(dropout)
        ) if project_out else nn.Identity()

    def forward(self, x):
        b, n, _, h = *x.shape, self.heads
        qkv = self.to_qkv(x).chunk(3, dim = -1)
        q, k, v = map(lambda t: rearrange(t, 'b n (h d) -> b h n d', h = h), qkv)
        dots = einsum('b h i d, b h j d -> b h i j', q, k) * self.scale
        attn = self.attend(dots)
        out = einsum('b h i j, b h j d -> b h i d', attn, v)
        out = rearrange(out, 'b h n d -> b n (h d)')
        return self.to_out(out)


# 基于PreNorm、Attention和FFN搭建Transformer
class Transformer(nn.Module):
    def __init__(self, dim, depth, heads, dim_head, mlp_dim, dropout = 0.):
        super().__init__()
        self.layers = nn.ModuleList([])
        for _ in range(depth):
            self.layers.append(nn.ModuleList([
                PreNorm(dim, Attention(dim, heads = heads, dim_head = dim_head, dropout = dropout)),
                PreNorm(dim, FeedForward(dim, mlp_dim, dropout = dropout))
            ]))
    def forward(self, x):
        for attn, ff in self.layers:
            x = attn(x) + x
            x = ff(x) + x
        return x


class ViT(nn.Module):
    def __init__(self, *, image_size, patch_size, num_classes, dim, depth, heads, 
                 mlp_dim, pool = 'cls', channels = 3, dim_head = 64,
                 dropout = 0., emb_dropout = 0.):
        super().__init__()
        image_height, image_width = pair(image_size)
        patch_height, patch_width = pair(patch_size)

        assert image_height % patch_height == 0 and image_width % patch_width == 0, 'Image dimensions must be divisible by the patch size.'
        # patch数量
        num_patches = (image_height // patch_height) * (image_width // patch_width)
        # patch维度
        patch_dim = channels * patch_height * patch_width
        assert pool in {'cls', 'mean'}, 'pool type must be either cls (cls token) or mean (mean pooling)'
        # 定义块嵌入
        self.to_patch_embedding = nn.Sequential(
            Rearrange('b c (h p1) (w p2) -> b (h w) (p1 p2 c)', p1 = patch_height, p2 = patch_width),
            nn.Linear(patch_dim, dim),
        )
        # 定义位置编码
        self.pos_embedding = nn.Parameter(torch.randn(1, num_patches + 1, dim))
        # 定义类别向量
        self.cls_token = nn.Parameter(torch.randn(1, 1, dim))
        self.dropout = nn.Dropout(emb_dropout)

        self.transformer = Transformer(dim, depth, heads, dim_head, mlp_dim, dropout)

        self.pool = pool
        self.to_latent = nn.Identity()
        # 定义MLP
        self.mlp_head = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, num_classes)
        )
        
    # ViT前向流程
    def forward(self, img):
        # 块嵌入
        x = self.to_patch_embedding(img)
        b, n, _ = x.shape
        # 追加类别向量
        cls_tokens = repeat(self.cls_token, '() n d -> b n d', b = b)
        x = torch.cat((cls_tokens, x), dim=1)
        # 追加位置编码
        x += self.pos_embedding[:, :(n + 1)]
        # dropout
        x = self.dropout(x)
        # 输入到transformer
        x = self.transformer(x)
        x = x.mean(dim = 1) if self.pool == 'mean' else x[:, 0]
        x = self.to_latent(x)
        # MLP
        return self.mlp_head(x)

```























































