[C++多线程详解（全网最全）](https://zhuanlan.zhihu.com/p/613630658)

# 多线程
<font style="color:rgb(25, 27, 31);">C++11标准之前，C++并没有引入线程这个概念，在C++11出来之前，如果我们想要在C++中实现多线程，需要借助操作系统平台提供的API，比如Linux的<pthread.h>，或者windows下的<windows.h> 。</font>

<font style="color:rgb(25, 27, 31);">C++11提供了语言层面上的多线程，包含在头文件<thread>中。它解决了跨平台的问题，提供了管理线程、保护共享数据、线程间同步操作、原子操作等类。C++11 新标准中引入了5个头文件来支持多线程编程，如下图所示：</font>

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710990632680-720132a5-95b9-4b86-a04c-a163a0854550.png)



## 多进程与多线程
### 多进程并发
### 多线程并发
<font style="color:rgb(25, 27, 31);">多线程并发指的是在同一个进程中执行多个线程。</font>

## 多线程的理解
## 创建线程
<font style="color:rgb(25, 27, 31);">创建线程很简单，只需要把函数添加到线程当中即可。</font>

+ <font style="color:rgb(25, 27, 31);">形式1：</font>

```cpp
std::thread myThread ( thread_fun);
//函数形式为void thread_fun()
myThread.join();
//同一个函数可以代码复用，创建多个线程
```

+ <font style="color:rgb(25, 27, 31);">形式2：</font>

```cpp
std::thread myThread ( thread_fun(100));
myThread.join();
//函数形式为void thread_fun(int x)
//同一个函数可以代码复用，创建多个线程
```

+ <font style="color:rgb(25, 27, 31);">形式3：</font>

```cpp
std::thread (thread_fun,1).detach();
//直接创建线程，没有名字
//函数形式为void thread_fun(int x)
```

## join与detach
<font style="color:rgb(25, 27, 31);">当线程启动后，一定要在和线程相关联的thread销毁前，确定以何种方式等待线程执行结束。比如上例中的join。</font>

+ <font style="color:rgb(25, 27, 31);">detach方式，启动的线程自主在后台运行，当前的代码继续往下执行，不等待新线程结束。</font>
+ <font style="color:rgb(25, 27, 31);">join方式，等待启动的线程完成，才会继续往下执行。</font>

<font style="color:rgb(25, 27, 31);"></font>

<font style="color:rgb(25, 27, 31);">可以使用joinable判断是join模式还是detach模式。</font>

```cpp
if (myThread.joinable()) 
    foo.join();
```

  


# mutex
<font style="color:rgb(25, 27, 31);">mutex头文件主要声明了与互斥量(mutex)相关的类。mutex提供了4种互斥类型，如下表所示。</font>

| <font style="color:rgb(25, 27, 31);">类型</font> | <font style="color:rgb(25, 27, 31);">说明</font> |
| :--- | :--- |
| <font style="color:rgb(25, 27, 31);">std::mutex</font> | <font style="color:rgb(25, 27, 31);">最基本的 Mutex 类。</font> |
| <font style="color:rgb(25, 27, 31);">std::recursive_mutex</font> | <font style="color:rgb(25, 27, 31);">递归 Mutex 类。</font> |
| <font style="color:rgb(25, 27, 31);">std::time_mutex</font> | <font style="color:rgb(25, 27, 31);">定时 Mutex 类。</font> |
| <font style="color:rgb(25, 27, 31);">std::recursive_timed_mutex</font> | <font style="color:rgb(25, 27, 31);">定时递归 Mutex 类。</font> |


<font style="color:rgb(25, 27, 31);">std::mutex 是C++11 中最基本的互斥量，std::mutex 对象提供了独占所有权的特性——即不支持递归地对 std::mutex 对象上锁，而 std::recursive_lock 则可以递归地对互斥量对象上锁。</font>

## <font style="color:rgb(25, 27, 31);">lock和unlock</font>
<font style="color:rgb(25, 27, 31);">mutex常用操作：</font>

+ <font style="color:rgb(25, 27, 31);">lock()：资源上锁</font>
+ <font style="color:rgb(25, 27, 31);">unlock()：解锁资源</font>
+ <font style="color:rgb(25, 27, 31);">trylock()：查看是否上锁，它有下列3种类情况：</font>

<font style="color:rgb(25, 27, 31);">（1）未上锁返回false，并锁住；</font>

<font style="color:rgb(25, 27, 31);">（2）其他线程已经上锁，返回true；</font>

<font style="color:rgb(25, 27, 31);">（3）同一个线程已经对它上锁，将会产生死锁。</font>

<font style="color:rgb(25, 27, 31);">死锁：是指两个或两个以上的进程在执行过程中，由于竞争资源或者由于彼此通信而造成的一种阻塞的现象，若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程。</font>

<font style="color:rgb(25, 27, 31);"></font>

<font style="color:rgb(25, 27, 31);">同一个mutex变量上锁之后，一个时间段内，只允许一个线程访问它。例如：</font>

```cpp
#include <iostream>  // std::cout
#include <thread>  // std::thread
#include <mutex>  // std::mutex

std::mutex mtx;  // mutex for critical section
void print_block (int n, char c) 
{
    // critical section (exclusive access to std::cout signaled by locking mtx):
    mtx.lock();
    for (int i=0; i<n; ++i) 
        {
            std::cout << c; 
        }
    std::cout << '\n';
    mtx.unlock();
}
int main ()
{
    std::thread th1 (print_block,50,'');//线程1：打印*
    std::thread th2 (print_block,50,'$');//线程2：打印$

    th1.join();
    th2.join();
    return 0;
}
```

<font style="color:rgb(25, 27, 31);">输出：</font>

```plain
**************************************************
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
```

<font style="color:rgb(25, 27, 31);">如果是不同mutex变量，因为不涉及到同一资源的竞争，所以以下代码运行可能会出现交替打印的情况，或者另一个线程可以修改共同的全局变量！</font>

```cpp
#include <iostream> // std::cout
#include <thread> // std::thread
#include <mutex> // std::mutex

std::mutex mtx_1; // mutex for critical section
std::mutex mtx_2;  // mutex for critical section
int test_num = 1;

void print_block_1 (int n, char c) 
{
    // critical section (exclusive access to std::cout signaled by locking mtx):
    mtx_1.lock();
    for (int i=0; i<n; ++i) 
        {
            //std::cout << c;
            test_num = 1;
            std::cout<<test_num<<std::endl;
        }
    std::cout << '\n';
    mtx_1.unlock();
}

void print_block_2 (int n, char c) 
{// critical section (exclusive access to std::cout signaled by locking mtx):
    mtx_2.lock();
    test_num = 2;
    for (int i=0; i<n; ++i) 
        {
            //std::cout << c;
            test_num = 2;
            std::cout<<test_num<<std::endl;
        }
    mtx_2.unlock();
}

int main ()
{
    std::thread th1 (print_block_1,10000,'*');
    std::thread th2 (print_block_2,10000,'$');

    th1.join();
    th2.join();
    return 0;
}
```

  


## <font style="color:rgb(25, 27, 31);">lock_guard</font>
<font style="color:rgb(25, 27, 31);">创建lock_guard对象时，它将尝试获取提供给它的互斥锁的所有权。当控制流离开lock_guard对象的作用域时，lock_guard析构并释放互斥量。lock_guard的特点：</font>

+ <font style="color:rgb(25, 27, 31);">创建即加锁，作用域结束自动析构并解锁，无需手工解锁</font>
+ <font style="color:rgb(25, 27, 31);">不能中途解锁，必须等作用域结束才解锁</font>
+ <font style="color:rgb(25, 27, 31);">不能复制</font>

```cpp
#include <thread>
#include <mutex>
#include <iostream>
int g_i = 0;
std::mutex g_i_mutex;  // protects g_i，用来保护g_i

void safe_increment()
{
    const std::lock_guard<std::mutex> lock(g_i_mutex);
    ++g_i;
    std::cout << std::this_thread::get_id() << ": " << g_i << '\n';// g_i_mutex自动解锁}int main(){
    std::cout << "main id: " <<std::this_thread::get_id()<<std::endl;
    std::cout << "main: " << g_i << '\n';

    std::thread t1(safe_increment);
    std::thread t2(safe_increment);

    t1.join();
    t2.join();

    std::cout << "main: " << g_i << '\n';
}
```

<font style="color:rgb(25, 27, 31);">说明：</font>

1. <font style="color:rgb(25, 27, 31);">该程序的功能为，每经过一个线程，g_i 加1。</font>
2. <font style="color:rgb(25, 27, 31);">因为涉及到共同资源g_i ，所以需要一个共同mutex：g_i_mutex。</font>
3. <font style="color:rgb(25, 27, 31);">main线程的id为1，所以下次的线程id依次加1。</font>

## unique_lock  



# <font style="color:rgb(25, 27, 31);">condition_variable</font>
# 线程池
## 概念
<font style="color:rgb(25, 27, 31);">在一个程序中，如果我们需要多次使用线程，这就意味着，需要多次的创建并销毁线程。而</font><u><font style="color:rgb(25, 27, 31);">创建并销毁线程的过程势必会消耗内存，线程过多会带来调动的开销，进而影响缓存局部性和整体性能。</font></u>

**<font style="color:rgb(25, 27, 31);">线程的创建并销毁有以下一些缺点：</font>**

+ <font style="color:rgb(25, 27, 31);">创建太多线程，将会浪费一定的资源，有些线程未被充分使用。</font>
+ <font style="color:rgb(25, 27, 31);">销毁太多线程，将导致之后浪费时间再次创建它们。</font>
+ <font style="color:rgb(25, 27, 31);">创建线程太慢，将会导致长时间的等待，性能变差。</font>
+ <font style="color:rgb(25, 27, 31);">销毁线程太慢，导致其它线程资源饥饿。</font>

<u><font style="color:rgb(25, 27, 31);">线程池维护着多个线程，这避免了在处理短时间任务时，创建与销毁线程的代价。</font></u>

## 线程池的实现
<font style="color:rgb(25, 27, 31);">因为程序边运行边创建线程是比较耗时的，所以我们通过池化的思想：</font><u><font style="color:rgb(25, 27, 31);">在程序开始运行前创建多个线程，这样，程序在运行时，只需要从线程池中拿来用就可以了。</font></u><font style="color:rgb(25, 27, 31);">大大提高了程序运行效率．一般线程池都会有以下几个部分构成：</font>

1. <font style="color:rgb(25, 27, 31);">线程池管理器（ThreadPoolManager）:用于创建并管理线程池，也就是线程池类</font>
2. <font style="color:rgb(25, 27, 31);">工作线程（WorkThread）: 线程池中线程</font>
3. <font style="color:rgb(25, 27, 31);">任务队列task: 用于存放没有处理的任务。提供一种缓冲机制。</font>
4. <font style="color:rgb(25, 27, 31);">append：用于添加任务的接口</font>

```cpp
#ifndef _THREADPOOL_H
#define _THREADPOOL_H
#include <vector>
#include <queue>
#include <thread>
#include <iostream>
#include <stdexcept>
#include <condition_variable>
#include <memory> //unique_ptr
#include<assert.h>

const int MAX_THREADS = 1000; //最大线程数目

template <typename T>
class threadPool
{
public:
threadPool(int number = 1);//默认开一个线程
~threadPool();
std::queue<T > tasks_queue; //任务队列
bool append(T *request);//往请求队列＜task_queue＞中添加任务<T >
private:
//工作线程需要运行的函数,不断的从任务队列中取出并执行
static void *worker(void arg);
void run();
private:
std::vector<std::thread> work_threads; //工作线程

std::mutex queue_mutex;
std::condition_variable condition;  //必须与unique_lock配合使用
bool stop;
};//end class//构造函数，创建线程
template <typename T>
threadPool<T>::threadPool(int number) : stop(false)
{
    if (number <= 0 || number > MAX_THREADS)
        throw std::exception();
    for (int i = 0; i < number; i++)
        {
            std::cout << "created Thread num is : " << i <<std::endl;
            work_threads.emplace_back(worker, this);
            //添加线程
            //直接在容器尾部创建这个元素，省去了拷贝或移动元素的过程。
        }
}
template <typename T>
inline threadPool<T>::~threadPool()
{
    std::unique_lock<std::mutex> lock(queue_mutex);
    stop = true;

    condition.notify_all();
    for (auto &ww : work_threads)
        ww.join();//可以在析构函数中join
}
//添加任务
template <typename T>
bool threadPool<T>::append(T *request)
{
    //操作工作队列时一定要加锁，因为他被所有线程共享
    queue_mutex.lock();//同一个类的锁
    tasks_queue.push(request);
    queue_mutex.unlock();
    condition.notify_one();  //线程池添加进去了任务，自然要通知等待的线程
    return true;
}//单个线程
template <typename T>
void threadPool<T>::worker(void *arg)
{
    threadPool pool = (threadPool *)arg;
    pool->run();//线程运行
    return pool;
}
template <typename T>
void threadPool<T>::run()
{
while (!stop)
{
    std::unique_lock<std::mutex> lk(this->queue_mutex);
    /*　unique_lock() 出作用域会自动解锁　/
    this->condition.wait(lk, [this] 
    { 
    return !this->tasks_queue.empty(); 
});//如果任务为空，则wait，就停下来等待唤醒//需要有任务，才启动该线程，不然就休眠
    if (this->tasks_queue.empty())//任务为空，双重保障
    {  
        assert(0&&"断了");//实际上不会运行到这一步，因为任务为空，wait就休眠了。
        continue;
    }else{
        T *request = tasks_queue.front();
        tasks_queue.pop();
        if (request)//来任务了，开始执行
            request->process();
    }
}
}
#endif
```

<font style="color:rgb(25, 27, 31);">说明：</font>

+ <font style="color:rgb(25, 27, 31);">构造函数创建所需要的线程数</font>
+ <font style="color:rgb(25, 27, 31);">一个线程对应一个任务，任务随时可能完成，线程则可能休眠，所以任务用队列queue实现（线程数量有限），线程用采用wait机制。</font>
+ <font style="color:rgb(25, 27, 31);">任务在不断的添加，有可能大于线程数，处于队首的任务先执行。</font>
+ <font style="color:rgb(25, 27, 31);">只有添加任务(append)后，才开启线程condition.notify_one()。</font>
+ <font style="color:rgb(25, 27, 31);">wait表示，任务为空时，则线程休眠，等待新任务的加入。</font>
+ <font style="color:rgb(25, 27, 31);">添加任务时需要添加锁，因为共享资源。</font>

