
## 1. Counter
`Counter`是`collections`模块提供的强大工具，用于高效统计列表、字符串、元组等可迭代对象中每个元素出现的次数，并返回一个**字典**。

### 1.1 常用方式
1.统计列表词频
```python
from collections import Counter
 
nums = [1, 1, 1, 6, 6, 6, 7, 8]
count = Counter(nums)  # 统计词频
for k, v in count.items():
    print(k, v)
print(count)
```

2.寻找出现次数最多的 k 个数
使用 **Counter** 统计完词频后可以使用 **most_common** 方法来查找出现频率最高的 k 个数字及其出现次数
```python
from collections import Counter
 
nums = [1, 1, 1, 6, 6, 6, 7, 8]
 
count = Counter(nums)
 
ansdict = count.most_common(2)  # 返回出现次数最多的两个数及其出现的次数
print(ansdict) # 注意输出格式
ans = []
for i in range(len(ansdict)):
    ans.append(ansdict[i][0])  # 提取出出现次数最多的两个数
print(ans)
```

### 1.2 

## 2. namedtuple()

## 3. deque

## 4. OrderedDict

## 5. defaultdict


