import time
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

def fibo(n):
    if n <= 1: return n
    else: return fibo(n-1) + fibo(n-2)

def main():
    start = time.perf_counter()
    nums = 41

    arr = [0] * nums

    # single threaded
    # for i in range (0, nums):
    #     print(i, end=" ", flush=True)
    #     arr[i] = fibo(i)

    # multithreading
    # with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
    #     # future_list = {executor.submit(fibo, i): i for i in range(0, nums)}
    #     future_list = {}
    #     for i in range(0, nums):
    #         print(i, end=" ", flush=True)
    #         future_list[executor.submit(fibo, i)] = i

    #     for future in as_completed(future_list):
    #         # print("completed", future_list[future])
    #         i = future_list[future]
    #         arr[i] = future.result()

    # multiprocessing
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        # future_list = {executor.submit(fibo, i): i for i in range(0, nums)}
        future_list = {}
        for i in range(0, nums):
            print(i, end=" ", flush=True)
            future_list[executor.submit(fibo, i)] = i

        for future in as_completed(future_list):
            # print("completed", future_list[future])
            i = future_list[future]
            arr[i] = future.result()


    print()
    print(arr)

    end = time.perf_counter()
    print(f"Total time: {end - start}")

if __name__ == "__main__":
    main()
