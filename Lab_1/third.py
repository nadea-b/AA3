import time
import matplotlib.pyplot as plt


def multiply(matrix1, matrix2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def power(matrix, n):
    result = [[1, 0], [0, 1]]  # Identity matrix
    while n > 0:
        if n % 2 == 1:
            result = multiply(result, matrix)
        matrix = multiply(matrix, matrix)
        n //= 2
    return result


def fibonacci_matrix(n):
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = power(base_matrix, n)
    return result_matrix[0][1]


# Given list of terms
terms = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849, 20897]

# Lists to store terms and corresponding time taken
term_list = []
time_list = []

for n in terms:
    start_time = time.time()  # Record start time
    fibonacci_value = fibonacci_matrix(n)  # Calculate Fibonacci value
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
plt.plot(term_list, time_list, marker='o', linestyle='-', color='lightblue')
plt.title('Time Taken to Calculate Fibonacci Value')
plt.xlabel('Term')
plt.ylabel('Time Taken (s)')
plt.grid(True)
plt.xticks(terms)  # Set x-axis ticks to match terms
plt.show()
