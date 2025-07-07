给你一个有序数组 `nums` ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素**只出现两次** ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

双指针时间复杂度O(n)，空间复杂度O(1)

``` python
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		n = len(nums)
		if n <= 2:
			return n
		p1, p2 = 1, 1
		
		while n > 1:
		n-=1
		if nums[p1-1] == nums[p1]:
			if nums[p1] == nums[p2]:
				p2 += 1
			else:
				nums[p1+1] = nums[p2]
				p1 += 1
			p2 += 1
		else:
			if p1 == p2:
				p2 += 1
			else:
				nums[p1+1] = nums[p2]
				p2 += 1
				p1 += 1
		return p1+1
```

Official solution：
```python
class Solution: 
	def removeDuplicates(self, nums: List[int]) -> int: 
		n = len(nums) 
		if n <= 2: 
			return n 
		slow, fast = 2, 2 
		while fast < n: 
			if nums[slow - 2] != nums[fast]: 
				nums[slow] = nums[fast] 
				slow += 1 
			fast += 1 
		return slow 
```
