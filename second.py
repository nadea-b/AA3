import time
import matplotlib.pyplot as plt


def fibonacci_dynamic(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Initialize an array to store Fibonacci numbers
    fib_array = [0] * (n + 1)
    fib_array[1] = 1

    # Calculate Fibonacci numbers from the bottom up
    for i in range(2, n + 1):
        fib_array[i] = fib_array[i - 1] + fib_array[i - 2]

    return fib_array[n]


# Given list of terms
terms = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]


# Lists to store terms and corresponding time taken
term_list = []
time_list = []

for n in terms:
    start_time = time.time()  # Record start time
    fibonacci_value = fibonacci_dynamic(n)  # Calculate Fibonacci value
    end_time = time.time()  # Record end time
    time_taken = end_time - start_time  # Calculate time taken
    term_list.append(n)  # Append term to list
    time_list.append(time_taken)  # Append time taken to list

#Output values
for term in term_list:
    print(f"{term:7}", end="")
print()

for time_val in time_list:
    print(f"{time_val:7.2f}", end="")
print()

# Plot the values
plt.figure(figsize=(10, 6))
plt.plot(term_list, time_list, marker='o', linestyle='-', color='pink')
plt.title('Time Taken to Calculate Fibonacci Value')
plt.xlabel('Term')
plt.ylabel('Time Taken (s)')
plt.grid(True)
plt.xticks(terms)  # Set x-axis ticks to match terms
plt.show()
