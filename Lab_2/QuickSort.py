import time
import matplotlib.pyplot as plt
import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Generate a random list of integers
random.seed(42)  # for reproducibility
n = 10000
arr = [random.randint(0, 100000) for _ in range(n)]

# Measure time taken for sorting
start_time = time.time()
quick_sort(arr, 0, n - 1)
end_time = time.time()

# Output time taken
print(f"Time taken to sort {n} elements using Quick Sort: {end_time - start_time:.6f} seconds")

# Plotting is omitted since it's not relevant for sorting algorithm comparisons
