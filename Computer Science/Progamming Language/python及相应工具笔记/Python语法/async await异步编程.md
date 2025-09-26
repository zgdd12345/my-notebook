## 1. Python 中的异步编程
* **重要概念：**
	* 协程（coroutine）：Coroutines are special functions that work similarly Python generators that on await they release the flow of control back to the event loop. A coroutine needs to be scheduled to run using the event loop, to do this we create a Task, which is a type of Future.
		1. <u>使用`async def`定义的函数是一个coroutine，这个函数内部可以用`await`关键字。</u>
		2. 使用`async def`定义的函数，调用之后返回的值，是一个coroutine对象，可以被用于`await`或者`asyncio.run`等。
		
		- 第一层含义是语法层面的概念，一个函数（一段代码）由`async def`定义，那么它就是一个coroutine。带来的效果是，这个函数内部可以用`await`。那么反过来就是说，一个普通的`def`定义的函数，内部不能用`await`，否则就会触发语法错误（SyntaxError）。
		 - 第二层含义是Python解释器运行时的概念，`coroutine`是Python解释器里内置的一个类。当我们调用`async def`定义的函数时，得到的返回值的类型就是`coroutine`。
		
		* 协程最重要的特性，在于多个协程可以同时`asyncio.sleep(1)`，现实世界只过去了1秒，而三个协程的时间都过去了1秒，从而节约了等待的时间。
	* `asyncio`里面，`await`的用法有两种：
		- `await coroutine`，就像普通的函数调用一样，执行coroutine对应的代码。
		- `await task`，中断当前代码的执行，event loop开始调度任务，直到`task`执行结束，恢复执行当前代码。
		- 当我们对一个coroutine使用`await`时，当前函数中断执行，Python解释器开始执行coroutine的代码，这和普通的函数调用没什么区别。
		- 
## 2. 异步函数
Python有四种函数：
```
# 1. 普通函数 FunctionType
def function():
    return 1
# 2. generator function ：GeneratorType
def generator():
    yield 2   # 生成器

# async修饰将普通函数和生成器函数包装成异步函数和异步生成器
# 3. 异步函数（协程） ：CoroutineType
async def async_function():
    return 3
# 4. 异步生成器 ： AsyncGeneratorType
async def async_function():
    yield 4

```
--- 

* 异步函数
* awaitable类
	实现了`__await__`方法的类。
* AsyncGenerator
    需要实现`__aiter__`和`__anext__`两个核心方法，以及 _asend_、_athro_ 、_aclose_ 方法。
*  async/await语法
	完成异步的代码不一定要用async/await；
	使用了async/await的代码也不一定能做到异步；
	async/await是协程的语法糖，使协程之间的调用变得更加清晰：
	使用async修饰的函数调用时会返回一个协程对象；
	await只能放在async修饰的函数里面使用；
	await后面必须要跟着一个协程对象或者Awaitable；
	**await的目的是等待协程控制流的返回；**
	实现暂停并挂起函数的操作的是yield；
- async作用
    常规函数开始执行后一直运行到`return`实现退出，如果需要能够中断的函数，就需要添加`async`关键字。
    `async`用来声明一个函数为异步函数，**异步函数**的特点就是能在函数执行过程中被挂起，去执行其他异步函数，等挂起条件消失后再回来执行。
* await作用
	`await`用来声明程序挂起。
	`await`后面只能跟异步程序或有`__await__`属性的对象。

	*两个异步程序async a、async b：*
	*a中一步有await，当程序碰到关键字await b后；*
	*异步程序a挂起，去执行异步b程序（就相当于从一个函数内部跳出去执行其他函数）；*
	*当挂起条件小时候，不管b是否执行完，要马上从b程序中跳出来，回到原程序a执行原来的操作；*
	*如果await后面跟的b函数不是异步函数，那么操作就只能等b执行完再返回，无法在b执行的过程中返回，这样就相当于直接调用b函数，没必要使用await关键字了。*
	*因此，需要await后面跟的是异步函数。*

## 3. Python并发之异步I/O(async,await)

	在Http请求方面，Python异步协程可以提交请求然后去做队列中其他等待的任务，让它慢慢请求，而不是传统的一直等它请求到完成为止，这样的话会浪费更多的时间与资源。总之异步编程能让你的代码在处于等待资源状态时处理其他任务。


