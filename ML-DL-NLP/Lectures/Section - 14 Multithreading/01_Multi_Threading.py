# When to use Multithreading?
# 1. When you have to perform I/O bound tasks
# 2. Concurrent execution of I/O bound tasks is a good use case for multithreading.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(0.5)
        print(f"Number: {i}")

def print_letters():
    for i in "abcde":
        time.sleep(0.5)
        print(f"Letter: {i}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()
# start the threads
t1.start()
t2.start()

# wait for the threads to finish
t1.join()
t2.join()

finished_time = time.time() - t
print(f"Time taken without threading: {finished_time}")