"""Real-World Example: Multiprocessing for CPU-bound Tasks

Scenario: Factorial Calculation

Factorial calculations, especially for large numbers, involve significant
computational work. Multiprocessing can be used to distribute the workload
across multiple CPU cores, improving performance."""

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000) # recursive factorial

def factorial(n):
    print(f"Calculating factorial of {n}")
    result = math.factorial(n)
    print(f"Factorial of {n} is : {result}")
    return result

if __name__ == "__main__":
    numbers = [5000, 6000, 7000, 8000, 9000, 10000]

    start = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)

    end = time.time()

    print(f"Time taken with multiprocessing: {end-start}")
    
