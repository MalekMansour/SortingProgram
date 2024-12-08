import tkinter as tk
from tkinter import ttk, messagebox

def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left_half = numbers[:mid]
        right_half = numbers[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                numbers[k] = left_half[i]
                i += 1
            else:
                numbers[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            numbers[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            numbers[k] = right_half[j]
            j += 1
            k += 1
    return numbers

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[0]
        less_than_pivot = [x for x in numbers[1:] if x <= pivot]
        greater_than_pivot = [x for x in numbers[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(numbers):
    n = len(numbers)
    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers, n, i)
    for i in range(n-1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)
    return numbers

def sort_numbers():
    try:
        numbers = list(map(int, entry.get().split(',')))
        algorithm = algo_combobox.get()
        if not algorithm:
            messagebox.showwarning("Warning", "Please select a sorting algorithm.")
            return

        if algorithm == "Selection Sort":
            result = selection_sort(numbers)
        elif algorithm == "Insertion Sort":
            result = insertion_sort(numbers)
        elif algorithm == "Bubble Sort":
            result = bubble_sort(numbers)
        elif algorithm == "Merge Sort":
            result = merge_sort(numbers)
        elif algorithm == "Quick Sort":
            result = quick_sort(numbers)
        elif algorithm == "Heap Sort":
            result = heap_sort(numbers)
        else:
            messagebox.showerror("Error", "Invalid algorithm selected.")
            return

        result_label.config(text="Sorted Numbers: " + ', '.join(map(str, result)))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers separated by commas.")

# GUI Setup
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("500x300")

# Input Entry
tk.Label(root, text="Enter numbers (comma-separated):").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Algorithm Selection
tk.Label(root, text="Select a sorting algorithm:").pack(pady=5)
algo_combobox = ttk.Combobox(root, values=[
    "Selection Sort", "Insertion Sort", "Bubble Sort", "Merge Sort", "Quick Sort", "Heap Sort"
], state="readonly")
algo_combobox.pack(pady=5)

# Sort Button
sort_button = tk.Button(root, text="Sort", command=sort_numbers)
sort_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()