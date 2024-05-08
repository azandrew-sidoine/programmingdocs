# Modern C++ (Parallelism & Concurrency) <thread>

## Basics

- std::thread

It's used to create an execution thread instance. It's the basics of concurrency in C++ concurrent programming.

```cpp
#include <iostream>
#include <thread>

int main()
{
    // Creates a new thread instance
    std::thread t{[] () {
        std::cout << "Running in thread: " << "Hello World" << std::endl;
    }};

    // Start or join the thread
    t.join();

    return 0;
}
```

## Mutex & Critical Section <mutex>

- std::mutex

It is the most basic mutex class in C++11, and you can create a mutex by instantiating std::mutex.

> std::mutex::lock() -> To lock a mutex
> std::mutex::unlock() -> To release a mutex lock

**Note**
In modern C++, avoid calling directly `lock()` a mutex, as we need to call `unlock()` if critical exception occurs. C++11 introduced a template class `std::lock_guard` for RAII implementation for mutexes which guarantees the exceptional security of the code, while keeping implementation simple.

```cpp
#include <iostream>
#include <thread>
#include <mutex>

int v = 1;

void critial_section(int change_v) 
{
    static std::mutex mtx;

    std::lock_guard<std::mutex> lock(mtx);

    // Execute contention work
    v = change_v;
    // Mutex is release after leaving the scope

    // unlock is automatically called even in case of
    // exception
}

int main()
{
    // Creates a new thread instance
    std::thread t1(critial_section, 2), t3(critial_section, 3);

    // Start or join the thread
    t1.join();
    t2.join();

    std::cout << v << std::endl;

    return 0;
}
```

- std::unique_lock

It's more flexible than `std::lock_guard` as it manages the locking and unlocking operation on `mutex` with exclusive ownership (no other `unique_lock` object owning the ownership of the `muxtex` object).

**Note**
It's recommended over `std::lock_guard` in most concurrent programming case.

**Note**
`std::lock_guard` cannot explicitly call lock and unlock, and `std::unique_lock` can be called anywhere after the declaration. It can reduce the scope of the lock and provide higher concurrency.

If were to use `std::condition_variable::wait`, we must use and `std::unique_lock`:


```cpp
#include <iostream>
#include <thread>
#include <mutex>

int v = 1;

void critial_section(int change_v) 
{
    static std::mutex mtx;

    std::unique_lock<std::mutex> lock(mtx);

    // Execute contention work
    v = change_v;
    // Print the changed value
    std::cout << v << std::endl;

    // Explicitly releasing lock
    lock.unlock();

    // Other are allowed to acquire lock

    // Before updating the shared memory
    // we acquire a new lock
    lock.lock();

    v += 1;
    std::cout << v << std::endl;

    // Lock is release when goes out of scope
}

int main()
{
    // Creates a new thread instance
    std::thread t1(critial_section, 2), t3(critial_section, 3);

    // Start or join the thread
    t1.join();
    t2.join();

    std::cout << v << std::endl;

    return 0;
}
```

## Future (std::future)

C++11 implementation of asynchronous tasks. Naturally, we can easily imagine it as a simple means of thread synchronization, namely the barrier.

- std::packaged_task

Wrap any target that can be called for asynchronous calls.

```cpp
#include <iostream>
#include <thread>
#include <future>

int main()
{
    // Create an object that returns an async value
    std::packaged_task<int()> task([]() { return 7; } );

    // Get the promise or future of task
    std::future<int> result = task.get_future(); // Run task in thread

    std::thread(std::move(task)).detach();

    std::cout << "Waiting...\n";

    result.wait(); // Block until future is resolved

    // Ge the result of the future
    std::cout << "Future done!: " << std::endl << "Result: " << result.get() << std::endl;
}
```

> std::future::wait() -> Block the main thread until task resolve
> std::future::get() -> Return the result of the future
> std::thread(std::packaged_task<T>) -> create a thread from an async call.

## Conditional variable

The condition variable std::condition_variable was born to solve the deadlock and was introduced when the mutex operation was not enough.

Example:

For example, a thread may need to wait for a condition
to be true to continue execution. A dead wait loop can cause all other threads to fail to enter the critical section so that when the condition is true, a deadlock occurs. Therefore, the `condition_variable`
instance is created primarily to wake up the waiting thread and avoid `deadlocks`.

> notify_one() -> Notify a single thread
> notify_all() -> notify all thread

```cpp
#include <queue>
#include <chrono>
#include <mutex>
#include <thread>
#include <iostream>
#include <condition_variable>

int main()
{
    std::queue<int> produced_nums;
    std::mutex mtx;

    std::condition_variable cond;
    bool notified = false; // Notify sign

    auto producer = [&]() {
        for (int i = 0; ; i++) {
            std::this_thread::sleep_for(std::chrono::milliseconds(500));

            std::unique_lock<std::mutex> = lock(mtx);

            std::cout << "Producing: " << i << std::endl;

            produced_nums.push(i);

            notified = true;

            cond.notify_all();
        }
    }

    auto consumer = [&]() {
        while(true) {
            std::unique_lock<std::mutex> lock(mtx);

            while(!notified) { // Avoid spurious wakeup
                cond.wait(lock);
            }
            // Temporal unlock to allow producer to produce more rather
            // than let consumer hold the lock until it consumed
            lock.unlock();
            std::this_thread::sleep_for(std::chrono::milliseconds(1000));
            lock.lock();

            if (!produced_nums.empty()) {
                std::cout << "consuming " << produced_nums.front() << std::endl;
                produced_nums.pop();
            }
            notified = false;
        }
    }

    std::thread p(producer);
    std::thread cs[2]; // List of consumers

    for (int i=0; i< 2; i++) {
        cs[i] = std::thread(consumer);
    }

    p.join();

    for (int i=0; i< 2; i++) {
        cs[i].join();
    }

    return 0;
}
```

## Atomic Operation & Memory Model

- Atomic operation `std::atomic`

std::mutex forces the rule of single operation at time as it's an OS level function:

-- It provides automatic state transition between threads, that's `lock` state
-- Only one thread read or write the shared variable memory when a `lock` is aquired.

C++11 multi-threaded `shared variable reading and writing`, introduced of the `std::atomic` template, so that we instantiate an `atomic type`, will be an atomic type read and write operations are minimized from a `set of instructions to a single CPU instruction`:

```cpp
#include <atomic>
#include <thread>
#include <iostream>

std::atomic<int> count = {0};

int main()
{
    std::thread t1([]() {
        count.fetch_add(1);
    });

    std::thread t2([]() {
        count++; // Identical to fetch add
        count += 1; // Identical to fetch add
    });

    t1.join();
    t2.join();

    std::cout << count << std::endl;

    return 0;
}
```

**Note**
Of course, not all types provide atomic operations because the feasibility of atomic operations depends on the architecture of the `CPU` and whether the type structure being instantiated satisfies the memory alignment requirements of the architecture, so we can always pass `std::atomic<T>::is_lock_free` to check if the atom type needs to support atomic operations:


```cpp
#include <atomic>
#include <thread>
#include <iostream>

struct A {
    float x;
    int y;
    long long z;
}

int main()
{
    std::atomic<A> a;

    // Check if the atomic variable support atomic operations
    std::cout << std::boolalpha << a.is_lock_free() << std::endl;

    return 0;
}
```

## Memory orders

To achieve the `ultimate performance` and `achieve consistency` of various strength requirements, `C++11` defines six different memory sequences for atomic operations.

- Relaxed model
Under this model, `atomic operations within a single thread are executed sequentially`, and instruction reordering is not allowed, `but the order of atomic operations between different threads is arbitrary`. The type is specified by `std::memory_order_relaxed`.

```cpp
std::atomic<int> counter = {0};
std::vector<std::thread> v;

for (int i = 0; i < 100; ++i) {
    v.emplace_back([&](){
        counter.fetch_add(1, std::memory_order_relaxed);
    });
}
```

- Release/consumption model
If a thread needs to modify a value, but another thread will have a dependency on that operation of the value, that is, the latter depends on the former.

```cpp
// Initialize as nullptr to prevent consumer to load a dangling pointer
std::atomic<int*> prt(nullptr);
int v;

std::thread producer([&]() {
    int* p = new int(42);
    v = 1024;
    // Write and Release the lock
    ptr.store(p, std::memory_order_release);
});

std::thread consumer([&]() {
    int* p = new int(42);
    // std::memory_order_consume ensures that consumer observe
    // producer when calling load
    // Only when producer produces
    while(!(p = ptr.load(std::memory_order_consume)));

    std::cout << "p: " << *p << std::endl;
    std::cout << "p: " << *p << std::endl;
});
```

- Release/Acquire model

Under this model, we can further `tighten the order of atomic operations between different threads`, specifying the timing between releasing `std::memory_order_release` and getting `std::memory_order_acquire`.

All write operation before release, it visible to other threads.

**Note**
`std::memory_order_release` (Backward barrier) insure that write before release does not happen after release operation.

`std::memory_order_acquire` ensures that a subsequent read or write after a acquire does not occur before the acquire operation.

`std::memory_order_acq_rel` option, combines the characteristics of the two barriers and determines a unique memory barrier, such that reads and writes of the current thread will not be rearranged across the barrier.

```cpp
std::vector<int> v;
std::atomic<int> flag = {0};

std::thread release([&]() {
    v.push_back(42);
    flag.store(1, std::memory_order_release);
});

std::thread acqrel([&]() {
    int expected = 1; // must before compare_exchange_strong
    // compare_exchange_strong: Compare-and-swap primitive, which has a weaker version, compare_exchange_weak, which allows a failure to be returned even if the exchange is successful
    while(!flag.compare_exchange_strong(expected, 2, std::memory_order_acq_rel)) {
        expected = 1; // must after compare_exchange_strong flag has changed to 2
    }
});

std::thread acquire([&]() {
    while(flag.load(std::memory_order_acquire) < 2);
    std::cout << v.at(0) << std::endl; // must be 42
});

release.join();
acqrel.join();
acquire.join();
```

- Sequential Consistent Model `std::memory_order_seq_cst`

Under this model, atomic operations satisfy sequence consistency, which in turn can cause performance loss.

```cpp
std::atomic<int> counter = {0};
std::vector<std::thread> v;
for (int i = 0; i < 100; ++i) {
    v.emplace_back([&](){
        counter.fetch_add(1, std::memory_order_seq_cst);
    });
}

for (auto& t: v) {
    t.join();
}
```
