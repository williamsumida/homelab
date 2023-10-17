# This script was created to learn how ThreadPoolExecutor works
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import random

ITEM_COUNT = 50


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        print("-----------------------------------------------------------------------")
        print(f"running {func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.4f} seconds to run.")
        return result

    return wrapper


def loop_task(n):
    for _ in range(n):
        ...


def time_task(n):
    time.sleep(n)


def get_test_case_list() -> list[int]:
    return [random.randint(1_000_000, 10_000_000) for _ in range(ITEM_COUNT)]


def get_time_test_case_list() -> list[int]:
    return [random.randint(0, 5) for _ in range(ITEM_COUNT)]


@timing_decorator
def running_without_parallelism(test_case_list: list[int], task_runner) -> None:
    # running without parallelism
    for test_case in test_case_list:
        task_runner(test_case)


@timing_decorator
def default_thread_pool_executor_config(test_case_list: list[int], task_runner) -> None:
    # with the default configurations
    with ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(task_runner, test_case_list)


@timing_decorator
def thread_pool_executor_with_100_workers(
    test_case_list: list[int], task_runner
) -> None:
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(task_runner, test_case_list)


@timing_decorator
def process_pool_executor_with_100_workers(
    test_case_list: list[int], task_runner
) -> None:
    with ProcessPoolExecutor(max_workers=100) as executor:
        executor.map(task_runner, test_case_list)


def main():
    test_case_list = get_test_case_list()
    print("testing for loop task")
    running_without_parallelism(test_case_list, loop_task)
    default_thread_pool_executor_config(test_case_list, loop_task)
    thread_pool_executor_with_100_workers(test_case_list, loop_task)
    # process_pool_executor_with_100_workers(test_case_list, loop_task)

    print("-----------------------------------------------------------------------")
    print("testing time task")
    test_case_list = get_time_test_case_list()
    running_without_parallelism(test_case_list, time_task)
    default_thread_pool_executor_config(test_case_list, time_task)
    thread_pool_executor_with_100_workers(test_case_list, time_task)
    # process_pool_executor_with_100_workers(test_case_list, time_task)


main()
