import random
import time
import matplotlib.pyplot as plt

# Implement the merge sort algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Random Data
def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Function to measure execution time of Merge Sort
def measure_merge_sort_time(arr):
    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()
    return end_time - start_time

# Visualize Execution Time using matplotlib.pyplot
def visualize_execution_time(sizes, execution_times):
    plt.plot(sizes, execution_times, marker='o')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (s)')
    plt.title('Merge Sort Execution Time')
    plt.show()

# Example usage:
sizes = [10, 100, 500, 1000, 5000, 10000]
execution_times = []

for size in sizes:
    data = generate_random_list(size)
    execution_time = measure_merge_sort_time(data)
    execution_times.append(execution_time)

visualize_execution_time(sizes, execution_times)
