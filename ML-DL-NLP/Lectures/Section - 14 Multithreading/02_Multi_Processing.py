# Multiprocessing
# Process that run in parallel
# CPU bound tasks
# Parallel execution of CPU bound tasks is a good use case for multiprocessing.
# Multiprocessing vs Multithreading: https://www.geeksforgeeks.org/multiprocessing-vs-multithreading-in-python/

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(0.5)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(0.5)
        print(f"Cube: {i*i*i}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    t = time.time()

    # start the processes
    p1.start()
    p2.start()

    # wait for the processes to finish
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(f"Time taken with multiprocessing: {finished_time}")
