#you can use 'time' to measure the time taken by each operation
import random
import time

# Create a list of objects
objects = [MyClass(random.randint(1, 100), random.randint(1, 100)) for i in range(75000)]

# Measure time for linear search
start_time = time.time()
result1 = linear_search(objects, 50)
result2 = linear_search(objects, 200)
linear_search_time = time.time() - start_time

# Measure time for insertion sort
start_time = time.time()
insertion_sort(objects)
insertion_sort_time = time.time() - start_time

# Measure time for built-in sort
start_time = time.time()
sorted(objects, key=lambda obj: obj.get_attr1())
builtin_sort_time = time.time() - start_time

# Measure time for linear search after sorting
start_time = time.time()
result3 = linear_search(objects, 50)
result4 = linear_search(objects, 200)
linear_search_after_sort_time = time.time() - start_time

# Measure time for binary search after sorting
start_time = time.time()
binary_search(objects, 50)
binary_search(objects, 200)
binary_search_time = time.time() - start_time

# Print the results
print(f"Linear search time: {linear_search_time}")
print(f"Insertion sort time: {insertion_sort_time}")
print(f"Built-in sort time: {builtin_sort_time}")
print(f"Linear search after sort time: {linear_search_after_sort_time}")
print(f"Binary search time: {binary_search_time}")
