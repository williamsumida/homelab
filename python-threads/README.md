# Understanding parallelism

In this scenario two classes were tested **ThreadPoolExecutor** and **ProcessPoolExecutor**.


Results:
```
testing for loop task
-----------------------------------------------------------------------
running running_without_parallelism
running_without_parallelism took 2.8901 seconds to run.
-----------------------------------------------------------------------
running default_thread_pool_executor_config
default_thread_pool_executor_config took 2.6571 seconds to run.
-----------------------------------------------------------------------
running thread_pool_executor_with_100_workers
thread_pool_executor_with_100_workers took 2.4134 seconds to run.
-----------------------------------------------------------------------
testing time task
-----------------------------------------------------------------------
running running_without_parallelism
running_without_parallelism took 129.1380 seconds to run.
-----------------------------------------------------------------------
running default_thread_pool_executor_config
default_thread_pool_executor_config took 129.1689 seconds to run.
-----------------------------------------------------------------------
running thread_pool_executor_with_100_workers
thread_pool_executor_with_100_workers took 5.0121 seconds to run.
```
