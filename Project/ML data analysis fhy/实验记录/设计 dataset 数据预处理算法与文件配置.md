
 
# 1.控制向量
 
- [ ]  标准化与归一化🔺 🛫 2025-09-12 ⏳ 2025-09-12 📅 2025-09-12
	代码：
```python
def standralize_ctrl_vertor(matrix: pd.DataFrame):
"""
标准化控制变量向量
matrix: pd.Dataframe, 控制变量向量
return: np.ndarray, 标准化后的控制变量向量
"""

norm_vec_range = [
{'max': 100,'min': 0,},
{'max': 650,'min': 5,},
{'max': 2500,'min': 10,},
{'max': 2000,'min': 1,},
{'max': 30,'min': 1,},
{'max': 30,'min': 5,},
{'max': 100,'min': 0,},
{'max': 650,'min': 5,},
{'max': 2500,'min': 10,},
{'max': 2000,'min': 1,},
{'max': 1.7,'min': 1.5,}, 
{'max': 30,'min': 0,},
{'max': 1500,'min': 1.5,},
{'max': 80,'min': 0.0002,},
{'max': 72.8,'min': 13,},
{'max': 100,'min': 50,}
]

scaler_std = StandardScaler()
res_norm_dic = {'壳体':{}, '中心爆管':{}, '药柱密度':{}, '挂高':{}, '装剂情况':{}}
res_std_dic = {'壳体':{}, '中心爆管':{}, '药柱密度':{}, '挂高':{}, '装剂情况':{}}

for col in matrix.columns:
	range_val = norm_vec_range[int(col)-1]['max'] - norm_vec_range[int(col)-1]['min']
	norm = (np.array(matrix[col]) - norm_vec_range[int(col)-1]['min'])/range_val
	std = scaler_std.fit_transform(norm.reshape(-1, 1))
	if 0 < col < 6:
		res_norm_dic['壳体'][col] = norm
		res_std_dic['壳体'][col] = std.flatten()
	elif 5 < col < 11:
		res_norm_dic['中心爆管'][col] = norm
		res_std_dic['中心爆管'][col] = std.flatten()
	elif col == 11:
		res_norm_dic['药柱密度'][col] = norm
		res_std_dic['药柱密度'][col] = std.flatten()
	elif col == 12:
		res_norm_dic['挂高'][col] = norm
		res_std_dic['挂高'][col] = std.flatten()
	elif 13 <= col <= 16:
		res_norm_dic['装剂情况'][col] = norm
		res_std_dic['装剂情况'][col] = std.flatten()
	else:
		raise ValueError("Column index out of range")

# pprint(res_std_dic.values())

return {'norm':res_norm_dic, 'std':res_std_dic}

```

- [ ] TODO

# 2.气象矩阵
- [ ]  风速🛫 2025-09-12⏫ 


风速（2米）、风向（2米），温度（2米，4米）、湿度（2米，4米）2米风向修正

## 2.1 风速

## 2.2 风向

## 2.3 风速与风向




