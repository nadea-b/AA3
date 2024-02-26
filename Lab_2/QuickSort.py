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

# Generate arrays of different dimensions
random.seed(42)
array_sizes = [1000, 10000, 100000, 500000, 1000000]
arrays = []

for size in array_sizes:
    arrays.append([random.randint(0, 100000) for _ in range(size)])

# Measure time taken for sorting each array
times = []

for arr in arrays:
    start_time = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end_time = time.time()
    times.append(end_time - start_time)

# Output time taken for each array
for size, time_taken in zip(array_sizes, times):
    print(f"Time taken to sort {size} elements using Quick Sort: {time_taken:.6f} seconds")

# Plotting
plt.plot(array_sizes, times, marker='o', linestyle='-', color = 'lightblue')
plt.title('Time Taken to Sort Arrays of Different Sizes')
plt.xlabel('Size of Array')
plt.ylabel('Time Taken (s)')
plt.grid(True)
plt.show()

