
--- 
tags: [LeetCode, 算法] 
date： 2025-07-09

--- 
**题目编号** : 
**难度** ⭐️⭐️   (中等)
**链接**: [链接](https://leetcode.cn/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150)
**标签**: #数组 #动态规划 #贪心    
## 题目描述 

给你一个非负整数数组 `nums` ，你最初位于数组的 **第一个下标** 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 `true` ；否则，返回 `false` 。

## 示例 
**示例 1：**
**输入：** nums = [2,3,1,1,4]
**输出：** true
**解释：**  可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

**示例 2：**
**输入：** nums = [3,2,1,0,4]
**输出：** false
**解释：** 无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

## 算法思想

在这里描述解题思路和算法思想


## Python 实现

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_length = 0
        n = len(nums)
        for i in range(n):
            if i <= max_length:
                max_length = max(nums[i] + i, max_length)
                if max_length >= n-1:
                    return True
            else:
                return False
        return False
        
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
