import time
import matplotlib.pyplot as plt


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# Given list of terms
terms = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]

# Lists to store terms and corresponding time taken
term_list = []
time_list = []

for n in terms:
    start_time = time.time()  # Record start time
    fibonacci_value = fibonacci_recursive(n)  # Calculate Fibonacci value
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
plt.plot(term_list, time_list, marker='o', linestyle='-', color='turquoise')
plt.title('Time Taken to Calculate Fibonacci Value')
plt.xlabel('Term')
plt.ylabel('Time Taken (s)')
plt.grid(True)
plt.xticks(terms)  # Set x-axis ticks to match terms
plt.show()
