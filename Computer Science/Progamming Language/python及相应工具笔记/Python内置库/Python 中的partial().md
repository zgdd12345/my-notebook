<font style="color:rgb(18, 18, 18);">Python 中的偏函数(functools.partial)</font>

---

**偏函数的作用：**

<font style="color:rgb(18, 18, 18);">和装饰器一样，它可以</font>**<font style="color:rgb(18, 18, 18);">扩展函数的功能</font>**<font style="color:rgb(18, 18, 18);">，但又不完全等价于装饰器。通常应用的场景是当我们要频繁调用某个函数时，其中某些参数是已知的固定值，通常我们可以调用这个函数多次，但这样看上去似乎代码有些冗余，而偏函数的出现就是为了解决这一个问题。</font>

---

**<font style="color:rgb(18, 18, 18);">偏函数的定义：</font>**

```python
func = functools.partial(func, *args, **keywords)
```

:::tips
func: 需要被扩展的函数，返回的函数其实是一个类 func 的函数  
*args: 需要被固定的位置参数  
**kwargs: 需要被固定的关键字参数

如果在原来的函数 func 中关键字不存在，将会扩展，如果存在，则会覆盖

:::



