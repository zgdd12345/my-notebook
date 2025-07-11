
--- 
tags: [LeetCode, 算法] 
 date: 2025-07-11

--- 
**题目编号** : 
**难度** ⭐️⭐️⭐️ (中等)   
**链接**: [链接](https://leetcode.cn/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150)
**标签**: #数组 #前缀和    
## 题目描述 

给你一个整数数组 `nums`，返回 数组 `answer` ，其中 `answer[i]` 等于 `nums` 中除 `nums[i]` 之外其余各元素的乘积 。

题目数据 **保证** 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在  **32 位** 整数范围内。

请 **不要使用除法，** 且在 `O(n)` 时间复杂度内完成此题。

## 示例 **示例 1:**

**输入:** nums = `[1,2,3,4]`
**输出:** `[24,12,8,6]`

**示例 2:**

**输入:** nums = [-1,1,0,-3,3]
**输出:** [0,0,9,0,0]

## 算法思想

计算前缀数组和后缀数组


## Python 实现

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, suf, res = [0]*n, [0]*n, [0]*n

        pre[0] = 1
        for i in range(1, n):
            pre[i] = nums[i-1] * pre[i-1]

        suf[n-1] = 1
        for i in range(n-2, -1, -1):
            suf[i] = nums[i + 1] * suf[i+1]

        for i in range(n):
            res[i] = pre[i] * suf[i]
        
        return res
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
