
--- 
tags: [LeetCode, 算法] 
date: 2025-07-09

--- 
**题目编号** : 
**难度** ⭐️⭐️⭐️ (中等)   
**链接**: [链接](https://leetcode.cn/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150)
**标签**: #数组 #贪心 #动态规划    
## 题目描述 

给定一个长度为 `n` 的 **0 索引**整数数组 `nums`。初始位置为 `nums[0]`。

每个元素 `nums[i]` 表示从索引 `i` 向后跳转的最大长度。换句话说，如果你在 `nums[i]` 处，你可以跳转到任意 `nums[i + j]` 处:

- `0 <= j <= nums[i]` 
- `i + j < n`

返回到达 `nums[n - 1]` 的最小跳跃次数。生成的测试用例可以到达 `nums[n - 1]`。

## 示例 

**示例 1:**
**输入:** nums = [2,3,1,1,4]
**输出:** 2
**解释:** 跳到最后一个位置的最小跳跃数是 `2`。
     从下标为 0 跳到下标为 1 的位置，跳 `1` 步，然后跳 `3` 步到达数组的最后一个位置。

**示例 2:**
**输入:** nums = [2,3,0,1,4]
**输出:** 2

## 算法思想

第一步可以到达一个区域2，计算该区域内的元素可到达最远点，得到区域3，区域3内所有元素可达到的最远点，得到区域4，以此类推到结束

具体实现中
1. 维护一个当前最远能够到达的下标位置，作为边界，到达边界时增加跳跃次数
2. 记录当前区域可达到的最远点，达到边界时，这个最远点就是下一个区域的边界。
3. 

## Python 实现

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        area, end, step = 0, 0, 0
        n = len(nums)

        for i in range(n-1):
            if area >= i:
                area = max(area, i + nums[i])
                if i == end:
                    end = area
                    step += 1
        return step

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

