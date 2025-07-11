
--- 
tags: [LeetCode, 算法] 
 {{date: 2025-07-10}}

--- 
**题目编号** : 
**难度** ⭐️⭐️⭐️ (中等)   
**链接**: [链接](https://leetcode.cn/problems/h-index/?envType=study-plan-v2&envId=top-interview-150)
**标签**: #数组 #计数排序 #排序   
## 题目描述 

给你一个整数数组 `citations` ，其中 `citations[i]` 表示研究者的第 `i` 篇论文被引用的次数。计算并返回该研究者的 **`h` 指数**。

根据维基百科上 [h 指数的定义](https://baike.baidu.com/item/h-index/3991452?fr=aladdin)：`h` 代表“高引用次数” ，一名科研人员的 `h` **指数** 是指他（她）至少发表了 `h` 篇论文，并且 **至少** 有 `h` 篇论文被引用次数大于等于 `h` 。如果 `h` 有多种可能的值，**`h` 指数** 是其中最大的那个。

## 示例 

**示例 1：**
**输入：**`citations = [3,0,6,1,5]`
**输出：** 3 
**解释：** 给定数组表示研究者总共有 `5` 篇论文，每篇论文相应的被引用了 `3, 0, 6, 1, 5` 次。
     由于研究者有 `3` 篇论文每篇 **至少** 被引用了 `3` 次，其余两篇论文每篇被引用 **不多于** `3` 次，所以她的 _h_ 指数是 `3`。

**示例 2：**
**输入：** citations = [1,3,1]
**输出：** 1

## 算法思想

方法一：排序
1. 先排序
2. 由H指数定义，至少有h篇文章引用大于等于h， h是其中最大的一个。
	1. 所以，第一个想法是维护一个h列表，排序后的数组中的每一个元素的h都算出来存进去，最好Max(h_list)即可。
	2. 而citations[i]的h为元素值或者在其之前还有多少个元素，

方法二：计数排序


## Python 实现

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_list = []
        for i, x in enumerate(citations):
            if x >= i+1:
                h_list.append(i+1)
            else:
                h_list.append(x)
        return max(h_list)


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, x in enumerate(citations):
            if x >= i+1:
                h = max(h, i + 1)
            else:
                h = max(h, x)
        return h

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, x in enumerate(citations):
            h = max(h, (min(x, i+1)))
        return h


# 计数排序
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counter = [0] * (n + 1)

        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        tot = 0
        for i in range(n, -1, -1):
            tot += counter[i]
            if tot >= i:
                return i
        return 0

```

## C++ 实现

```cpp

{{C++ 代码实现}}
```

## 复杂度分析

- 时间复杂度: O()
- 空间复杂度: O()

## 相似题目

- [题目名称](https://chat.baidu.com/%E9%93%BE%E6%8E%A5)
- [题目名称](https://chat.baidu.com/%E9%93%BE%E6%8E%A5)

## 笔记

个人思考和总结
