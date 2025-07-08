
--- 
tags: [LeetCode, 算法] 
date: 2025-07-09

--- 
# 买卖股票的最佳时机2
**题目编号** : 122
**难度** ⭐️⭐️⭐️ (中等)   
**链接**: [链接](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150)
**标签**: #数组 #贪心 #动态规划    
## 题目描述 

给你一个整数数组 `prices` ，其中 `prices[i]` 表示某支股票第 `i` 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 **最多** 只能持有 **一股** 股票。你也可以先购买，然后在 **同一天** 出售。

返回 _你能获得的 **最大** 利润_ 。

## 示例 
```plaintext 
输入:  
输出:  
解释:
```
## 算法思想

我的思路：
只要当前和前面的价格有价格差就有利润
每卖一次就是重新开始，更新当前价格为初始价格。


## Python 实现

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        res = 0
        for cur in prices[1:]:
            if cur > min_price:
                res += cur - min_price
            min_price = cur
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
