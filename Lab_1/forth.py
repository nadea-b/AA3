import time
import matplotlib.pyplot as plt
from decimal import Decimal


def fibonacci_binet(n):
    phi = (1 + Decimal(5).sqrt()) / 2
    phi1 = (1 - Decimal(5).sqrt()) / 2
    return (phi**n - phi1**n) / (Decimal(2)**n * Decimal(5).sqrt())


# Given list of terms
terms = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849, 20897]

# Lists to store terms and corresponding time taken
term_list = []
time_list = []

for n in terms:
    start_time = time.time()  # Record start time
    fibonacci_value = fibonacci_binet(n)  # Calculate Fibonacci value
    end_time = time.time()  # Record end time
    time_taken = end_time - start_time  # Calculate time taken
    term_list.append(n)  # Append term to list
    time_list.append(time_taken)  # Append time taken to list

# Output values
for term in term_list:
    print(f"{term:8}", end="")
print()

for time_val in time_list:
    print(f"{time_val:8.5f}", end="")
print()

# Plot the values only for the last set of results
plt.figure(figsize=(10, 6))
plt.plot(term_list, time_list, marker='o', linestyle='-', color='yellow')
plt.title('Time Taken to Calculate Fibonacci Value')
plt.xlabel('Term')
plt.ylabel('Time Taken (s)')
plt.grid(True)
plt.xticks(terms)  # Set x-axis ticks to match terms
plt.show()