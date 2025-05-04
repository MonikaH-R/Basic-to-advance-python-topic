import random
import string
import time

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x.lower() <= pivot.lower()]
    greater = [x for x in arr[1:] if x.lower() > pivot.lower()]
    return quick_sort(less) + [pivot] + quick_sort(greater)

# Helper function to generate random strings
def generate_random_strings(n, str_length=6):
    return [''.join(random.choices(string.ascii_lowercase, k=str_length)) for _ in range(n)]

# Test the quick sort on different input sizes
for size in [1000, 10000, 20000]:
    strings = generate_random_strings(size)
    print(f"\nSorting {size} random strings...")

    start_time = time.time()
    sorted_strings = quick_sort(strings)
    end_time = time.time()

    print(f"First 5 sorted strings: {sorted_strings[:5]}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
