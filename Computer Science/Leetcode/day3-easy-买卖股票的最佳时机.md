
--- 
tags: [LeetCode, 算法] 
date: 2025-07-08 
--- 
# 题目名称 
**题目编号** : 121
**难度** ⭐️⭐️ 
**链接**: [链接](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150)
**标签**: #数组 #动态规划    
## 题目描述 

给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

## 示例 
```plaintext 
输入:  
输出:  
解释:
```
## 算法思想

算是最简单的动态规划？

以卖出时间为当前点，往前找最低价格，就是当前的最佳卖出点，也就可以获得最大利润。
所以循环的时候记录前面的最低价格即可。

所以时间复杂度O(n)

![[bestprice1.png]]

## Python 实现


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]
        for i, sell in enumerate(prices[1:]):
            if min_price > sell:
                min_price = sell
            else:
                profit = sell - min_price
                if profit > res:
                    res = profit

        return res
```

## C++ 实现

```cpp

{{C++ 代码实现}}
```

## 复杂度分析

- 时间复杂度: O(n)
- 空间复杂度: O(1)

## 相似题目

- [题目名称](https://chat.baidu.com/%E9%93%BE%E6%8E%A5)
- [题目名称](https://chat.baidu.com/%E9%93%BE%E6%8E%A5)

## 笔记

个人思考和总结
