import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Sorting Algorithms with Steps
def bubble_sort(numbers):
    steps = []
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            steps.append(f"Comparing {numbers[j]} and {numbers[j + 1]}")
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                steps.append(f"Swapped: {numbers}")
    return numbers, steps

def selection_sort(numbers):
    steps = []
    n = len(numbers)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps.append(f"Comparing {numbers[j]} and {numbers[min_idx]}")
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        steps.append(f"Swapped {numbers[i]} with {numbers[min_idx]}: {numbers}")
    return numbers, steps

def insertion_sort(numbers):
    steps = []
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        steps.append(f"Insert {key} into sorted part")
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            steps.append(f"Moved {numbers[j]} to position {j + 1}")
            j -= 1
        numbers[j + 1] = key
        steps.append(f"Inserted {key} at position {j + 1}: {numbers}")
    return numbers, steps

def merge_sort(numbers):
    steps = []

    def merge_sort_recursive(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            merge_sort_recursive(left)
            merge_sort_recursive(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    steps.append(f"Added {left[i]} from left to position {k}")
                    i += 1
                else:
                    arr[k] = right[j]
                    steps.append(f"Added {right[j]} from right to position {k}")
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                steps.append(f"Added remaining {left[i]} to position {k}")
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                steps.append(f"Added remaining {right[j]} to position {k}")
                j += 1
                k += 1

    merge_sort_recursive(numbers)
    return numbers, steps

def quick_sort(numbers):
    steps = []

    def quick_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        steps.append(f"Pivot chosen: {pivot}")
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        steps.append(f"Partitioned to left: {left}, middle: {middle}, right: {right}")
        return quick_sort_recursive(left) + middle + quick_sort_recursive(right)

    sorted_numbers = quick_sort_recursive(numbers)
    return sorted_numbers, steps

def heap_sort(numbers):
    steps = []

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            steps.append(f"Swapped {arr[i]} with {arr[largest]}: {arr}")
            heapify(arr, n, largest)

    n = len(numbers)
    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers, n, i)
    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        steps.append(f"Swapped {numbers[i]} with {numbers[0]}: {numbers}")
        heapify(numbers, i, 0)

    return numbers, steps

def radix_sort(numbers):
    steps = []

    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in arr:
            index = (i // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]

    max_num = max(numbers)
    exp = 1
    while max_num // exp > 0:
        steps.append(f"Sorting by place value {exp}")
        counting_sort(numbers, exp)
        steps.append(f"Array after sorting by {exp}: {numbers}")
        exp *= 10

    return numbers, steps

def swap_sort(numbers):
    steps = []
    n = len(numbers)
    for i in range(n):
        while 1 <= numbers[i] <= n and numbers[numbers[i] - 1] != numbers[i]:
            correct_index = numbers[i] - 1
            steps.append(f"Swapping {numbers[i]} with {numbers[correct_index]}")
            numbers[correct_index], numbers[i] = numbers[i], numbers[correct_index]
            steps.append(f"Array after swap: {numbers}")
    return numbers, steps

def shell_sort(numbers):
    steps = []  # To store the steps of the sorting process
    n = len(numbers)
    gap = n // 2
    steps.append(f"Starting list: {numbers}")  # Initial list

    while gap > 0:
        steps.append(f"Gap: {gap}")  # Current gap value
        for i in range(gap, n):
            current_value = numbers[i]
            j = i
            steps.append(f"Considering element {current_value} at index {i}")
            while j >= gap and numbers[j - gap] > current_value:
                numbers[j] = numbers[j - gap]
                steps.append(f"Swapped {numbers[j]} with {numbers[j - gap]} -> {numbers}")
                j -= gap
            numbers[j] = current_value
            steps.append(f"Inserted {current_value} at index {j} -> {numbers}")
        gap //= 2  # Reduce gap

    steps.append(f"Final Sorted List: {numbers}")
    return numbers, steps

# Main Sorting Function
def sort_numbers():
    try:
        input_text = input_text_box.get("1.0", tk.END).strip()
        numbers = list(map(int, input_text.split(",")))
        sort_method = sort_method_combo.get()

        if sort_method == "Bubble Sort":
            result, steps = bubble_sort(numbers)
        elif sort_method == "Swap Sort":
            result, steps = swap_sort(numbers)
        elif sort_method == "Shell Sort":
            result, steps = shell_sort(numbers)
        elif sort_method == "Selection Sort":
            result, steps = selection_sort(numbers)
        elif sort_method == "Insertion Sort":
            result, steps = insertion_sort(numbers)
        elif sort_method == "Merge Sort":
            result, steps = merge_sort(numbers)
        elif sort_method == "Quick Sort":
            result, steps = quick_sort(numbers)
        elif sort_method == "Heap Sort":
            result, steps = heap_sort(numbers)
        elif sort_method == "Radix Sort":
            result, steps = radix_sort(numbers)
        elif sort_method == "Inverse Sort":
            result = sorted(numbers, reverse=True)
            steps = [f"Sorting in descending order: {result}"]
        else:
            raise ValueError("Invalid sorting method selected.")

        # Display the sorted result
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, ", ".join(map(str, result)))

        # Display the steps
        explanation_text_box.delete("1.0", tk.END)
        explanation_text_box.insert(tk.END, "\n".join(steps))

    except ValueError as ve:
        messagebox.showerror("Error", f"Invalid input or sorting method: {ve}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Clear All Function
def clear_all():
    input_text_box.delete("1.0", tk.END)
    output_text_box.delete("1.0", tk.END)
    explanation_text_box.delete("1.0", tk.END)

# Create Tkinter Window
root = tk.Tk()
root.title("Sorting Program with Explanations")

# Layout Configuration
root.rowconfigure(0, weight=1)
root.columnconfigure([0, 1, 2], weight=1, uniform="column")

# Input Text Area
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.grid(row=0, column=0, sticky="nsew")
tk.Label(input_frame, text="Input Numbers (comma-separated):", anchor="w").pack(fill="x")
input_text_box = tk.Text(input_frame, height=20, width=40)
input_text_box.pack(fill="both", expand=True)

# Controls
controls_frame = tk.Frame(root, padx=10, pady=10)
controls_frame.grid(row=0, column=1, sticky="nsew")

# Dropdown to select sorting method
sort_method_combo = ttk.Combobox(controls_frame, state="readonly", values=[
    "Bubble Sort", "Swap Sort", "Shell Sort", "Selection Sort", "Insertion Sort",
    "Merge Sort", "Quick Sort", "Heap Sort", "Radix Sort", "Inverse Sort"])
sort_method_combo.set("Bubble Sort")
sort_method_combo.pack(fill="x", pady=5)

# Sort button
sort_button = tk.Button(controls_frame, text="Sort", command=sort_numbers)
sort_button.pack(fill="x", pady=5)

# Clear All button
clear_button = tk.Button(controls_frame, text="Clear All", command=clear_all)
clear_button.pack(fill="x", pady=5)

# Clear All function
def clear_all():
    input_text_box.delete("1.0", tk.END)
    output_text_box.delete("1.0", tk.END)
    explanation_text_box.delete("1.0", tk.END)
    sort_method_combo.set("Bubble Sort") 

# Explanation Box
explanation_frame = tk.Frame(controls_frame, padx=10, pady=10)
explanation_frame.pack(fill="both", expand=True)
tk.Label(explanation_frame, text="Explanation of Steps:", anchor="w").pack(fill="x")
explanation_text_box = tk.Text(explanation_frame, height=10, wrap="word")
explanation_text_box.pack(fill="both", expand=True)

# Output Text Area
output_frame = tk.Frame(root, padx=10, pady=10)
output_frame.grid(row=0, column=2, sticky="nsew")
tk.Label(output_frame, text="Sorted Output:", anchor="w").pack(fill="x")
output_text_box = tk.Text(output_frame, height=20, width=40)
output_text_box.pack(fill="both", expand=True)

root.mainloop()
