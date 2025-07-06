给你两个按 **非递减顺序** 排列的整数数组 `nums1` 和 `nums2`，另有两个整数 `m` 和 `n` ，分别表示 `nums1` 和 `nums2` 中的元素数目。

请你 **合并** `nums2` 到 `nums1` 中，使合并后的数组同样按 **非递减顺序** 排列。

注意： 最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况，`nums1` 的初始长度为 `m + n`，其中前 `m` 个元素表示应合并的元素，后 `n` 个元素为 `0` ，应忽略。`nums2` 的长度为 `n` 。
## 解法1

直接合并后排序

## 解法2 双指针

数组 nums 1与 nums 2已经被排序。为了利用这一性质，我们可以使用双指针方法。这一方法将两个数组看作队列，每次从两个数组头部取出比较小的数字放到结果中。

第一次写的：时间还行，内存占用偏大，列表操作对内存不友好。
```python
class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		q1 = nums1[:m]
		q2 = nums2[:n]
		res = []
		
		while len(q1) > 0 and len(q2) > 0:
			if q1[0] > q2[0]:
				res.append(q2.pop(0))
			else:
				res.append(q1.pop(0))
		
		if len(q1) > 0:
			res.extend(q1)	
			nums1[:len(res)] = res
		elif len(q2) > 0:
			res.extend(q2)
			nums1[:] = res
```
