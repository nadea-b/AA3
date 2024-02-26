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

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Generate arrays of different dimensions
random.seed(42)
array_sizes = [1000, 10000, 100000, 500000, 1000000]
arrays = []

for size in array_sizes:
    arrays.append([random.randint(0, 100000) for _ in range(size)])

# Measure time taken for sorting each array using Quick Sort
quick_sort_times = []

for arr in arrays:
    start_time = time.time()
    quick_sort(arr.copy(), 0, len(arr) - 1)
    end_time = time.time()
    quick_sort_times.append(end_time - start_time)

# Measure time taken for sorting each array using Merge Sort
merge_sort_times = []

for arr in arrays:
    start_time = time.time()
    merge_sort(arr.copy())
    end_time = time.time()
    merge_sort_times.append(end_time - start_time)

# Measure time taken for sorting each array using Heap Sort
heap_sort_times = []

for arr in arrays:
    start_time = time.time()
    heap_sort(arr.copy())
    end_time = time.time()
    heap_sort_times.append(end_time - start_time)

# Measure time taken for sorting each array using Timsort
timsort_times = []

for arr in arrays:
    start_time = time.time()
    arr.sort()  # Using Python's built-in Timsort
    end_time = time.time()
    timsort_times.append(end_time - start_time)

# Output time taken for each array
for size, quick_sort_time, merge_sort_time, heap_sort_time, timsort_time in zip(array_sizes, quick_sort_times, merge_sort_times, heap_sort_times, timsort_times):
    print(f"Time taken to sort {size} elements using Quick Sort: {quick_sort_time:.6f} seconds")
    print(f"Time taken to sort {size} elements using Merge Sort: {merge_sort_time:.6f} seconds")
    print(f"Time taken to sort {size} elements using Heap Sort: {heap_sort_time:.6f} seconds")
    print(f"Time taken to sort {size} elements using Timsort: {timsort_time:.6f} seconds")

# Plotting
plt.plot(array_sizes, quick_sort_times, marker='o', linestyle='-', color='lightblue', label='Quick Sort')
plt.plot(array_sizes, merge_sort_times, marker='o', linestyle='-', color='lightgreen', label='Merge Sort')
plt.plot(array_sizes, heap_sort_times, marker='o', linestyle='-', color='yellow', label='Heap Sort')
plt.plot(array_sizes, timsort_times, marker='o', linestyle='-', color='lightpink', label='Timsort')
plt.title('Time Taken to Sort Arrays of Different Sizes')
plt.xlabel('Size of Array')
plt.ylabel('Time Taken (s)')
plt.legend()
plt.grid(True)
plt.show()
