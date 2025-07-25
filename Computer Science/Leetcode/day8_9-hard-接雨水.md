
--- 
tags: [LeetCode, 算法] 
date:2025-07-13

--- 
**题目编号** : 42
**难度** ⭐️⭐️⭐️⭐️ (难)   
**链接**: [链接](https://leetcode.cn/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150)
**标签**: #数组 #栈 #双指针 #动态规划 #单调栈    
# 题目描述 

给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

## 示例 

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png)

**输入：** height = [0,1,0,2,1,0,1,3,2,1,2,1]
**输出：** 6
**解释：** 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

**示例 2：**

**输入：** height = [4,2,0,3,2,5]
**输出：** 9

# 方法一 动态规划-面积
### 算法思想
#动态规划 
方法一：计算包含雨水的面积，再减去数组的面积。
	面积计算，找到最高点，计算最高点左右的面积，再加最高点之间的面积即可

### Python 实现

```python
class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0
        dic = {}
        for i, h in enumerate(height):
            if h in dic:
                dic[h].append(i)
            else:
                dic[h] = [i]
        tallest_index = max(dic.keys())
        if len(dic[tallest_index]) > 1:
            tallest_list = sorted(dic[tallest_index])
            # print(dic[tallest_index])
            # print(tallest_index, tallest_list)
            res += (tallest_list[-1] - tallest_list[0] + 1) * tallest_index

            left_res = self.left_area(tallest_list[0], height)
            right_res = self.right_area(tallest_list[-1], height)
            return res + left_res + right_res - sum(height)
        else:
            tallest_list = dic[tallest_index]
            left_res = self.left_area(tallest_list[0], height)
            right_res = self.right_area(tallest_list[-1], height)
            return left_res + right_res + tallest_index - sum(height)
        

        
    def left_area(self, end, height):
        if len(height[:end]) < 1:
            return 0
        res = 0
        last_h = 0
        for i, h in enumerate(height[:end]):
            # last_h = max(last_h, h)
            if h > last_h:
                # last_h = h
                res += (h-last_h)*(end-i)
                last_h = h
                # print(res)
        # print('left:', res)
        return res

    def right_area(self, start, height):
        if len(height[start:]) < 1:
            return 0
        res = 0
        last_h = 0
        height_list = height[start+1:][::-1]
        # print(height_list)
        for i, h in enumerate(height_list):
            # last_h = max(last_h, h)
            if h > last_h:
                # last_h = h
                res += (h-last_h)*(len(height_list)-i)
                last_h = h
        # print('right:', res)
        return res



```

## C++ 实现

```cpp

{{C++ 代码实现}}
```

## 复杂度分析

- 时间复杂度: O(n)
- 空间复杂度: O(n)

# 方法二 动态规划
### 算法思想

#动态规划 

	对于下标 i，下雨后水能到达的最大高度等于下标 i 两边的最大高度的最小值，下标 i 处能接的雨水量等于下标 i 处的水能到达的最大高度减去 height[i]。
	所以后续的问题是怎么找到每个i的左右最大高度。
	方法一：暴力法，对每个i像左右找最高点
	方法二：动态规划
		得到left_max数组和right_max数组存储height[i]左边和右边的最大值
	最后， 
	
$$
 \sum_{i}^{len(height)}min(left\_max[i],right\_max[i]) - height[i]  
$$
### Python 实现

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max,right_max = [], []

        max_h = 0
        for h in height:
            max_h = max(h, max_h)
            left_max.append(max_h)
        
        max_h = 0
        for h in height[::-1]:
            max_h = max(h, max_h)
            right_max.append(max(h, max_h))
        right_max = right_max[::-1]

        res = 0
        for i in range(len(height)):
            res += min(left_max[i], right_max[i]) - height[i]
        
        return res

```

### C++ 实现

```cpp

{{C++ 代码实现}}
```

### 复杂度分析

- 时间复杂度: O(n)
- 空间复杂度: O(n)


# 方法三 单调栈
[[单调栈]]
### 算法思想
#单调栈 
维护一个单调栈，单调栈存储的是下标，满足从栈底到栈顶的下标对应的数组 height 中的元素递减。

从左到右遍历数组，遍历到下标 i 时，如果栈内至少有两个元素，记栈顶元素为 top，top 的下面一个元素是 left，则一定有 height[left]≥height[top]。如果 height[i]>height[top]，则得到一个可以接雨水的区域，该区域的宽度是 i−left−1，高度是 min(height[left],height[i])−height[top]，根据宽度和高度即可计算得到该区域能接的雨水量。

为了得到 left，需要将 top 出栈。在对 top 计算能接的雨水量之后，left 变成新的 top，重复上述操作，直到栈变为空，或者栈顶下标对应的 height 中的元素大于或等于 height[i]。

在对下标 i 处计算能接的雨水量之后，将 i 入栈，继续遍历后面的下标，计算能接的雨水量。遍历结束之后即可得到能接的雨水总量。

### Python 实现

```python

{{Python 代码实现}}
```

### C++ 实现

```cpp

{{C++ 代码实现}}
```

### 复杂度分析

- 时间复杂度: O()
- 空间复杂度: O()

# 方法四 双指针
### 算法思想
#双指针 



### Python 实现

```python

{{Python 代码实现}}
```

### C++ 实现

```cpp

{{C++ 代码实现}}
```

### 复杂度分析

- 时间复杂度: O()
- 空间复杂度: O()





# 相似题目

- [题目名称](https://chat.baidu.com/%E9%93%BE%E6%8E%A5)
- [题目名称](https://chat.baidu.com/%E9%93%BE%E6%8E%A5)
