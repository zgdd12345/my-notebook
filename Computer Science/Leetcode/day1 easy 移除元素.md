有点简单
``` python
class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		res = []
		k = 0
		for i, x in enumerate(nums):
			if x != val:
			res.append(x)
		nums[:] = res[:]
		return len(res)
```

修改后，原地操作

```python
class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		res = []
		k = 0
		for i, x in enumerate(nums):
			if x != val:
			res.append(x)
		nums[:] = res[:]
		return len(res)
```

