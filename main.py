import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Sorting Algorithms
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def swap_sort(numbers):
    n = len(numbers)
    for i in range(n):
        while 1 <= numbers[i] <= n and numbers[numbers[i] - 1] != numbers[i]:
            correct_index = numbers[i] - 1
            numbers[correct_index], numbers[i] = numbers[i], numbers[correct_index]
    return numbers

def shell_sort(numbers):
    n = len(numbers)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j - gap]
                j -= gap
            numbers[j] = temp
        gap //= 2
    return numbers

def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
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

def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        L = numbers[:mid]
        R = numbers[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                numbers[k] = L[i]
                i += 1
            else:
                numbers[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            numbers[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            numbers[k] = R[j]
            j += 1
            k += 1
    return numbers

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def radix_sort(numbers):
    max_val = max(numbers)
    exp = 1
    while max_val // exp > 0:
        counting_sort(numbers, exp)
        exp *= 10
    return numbers

def counting_sort(numbers, exp):
    n = len(numbers)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = numbers[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = numbers[i] // exp
        output[count[index % 10] - 1] = numbers[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        numbers[i] = output[i]

def inverse_sort(numbers):
    return sorted(numbers, reverse=True)

# Main Sorting Function
def sort_numbers():
    try:
        input_text = input_text_box.get("1.0", tk.END).strip()
        numbers = list(map(int, input_text.split(",")))
        sort_method = sort_method_combo.get()

        if sort_method == "Bubble Sort":
            result = bubble_sort(numbers)
        elif sort_method == "Swap Sort":
            result = swap_sort(numbers)
        elif sort_method == "Shell Sort":
            result = shell_sort(numbers)
        elif sort_method == "Selection Sort":
            result = selection_sort(numbers)
        elif sort_method == "Insertion Sort":
            result = insertion_sort(numbers)
        elif sort_method == "Merge Sort":
            result = merge_sort(numbers)
        elif sort_method == "Quick Sort":
            result = quick_sort(numbers)
        elif sort_method == "Radix Sort":
            result = radix_sort(numbers)
        elif sort_method == "Inverse Sort":
            result = inverse_sort(numbers)
        else:
            raise ValueError("Invalid sorting method selected.")

        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, ", ".join(map(str, result)))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Clear All Function
def clear_all():
    input_text_box.delete("1.0", tk.END)
    output_text_box.delete("1.0", tk.END)

# Create Tkinter Window
root = tk.Tk()
root.title("Sorting Program")

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
sort_method_combo = ttk.Combobox(controls_frame, state="readonly", values=[
    "Bubble Sort", "Swap Sort", "Shell Sort", "Selection Sort", 
    "Insertion Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Inverse Sort"])
sort_method_combo.set("Bubble Sort")
sort_method_combo.pack(fill="x", pady=5)
sort_button = tk.Button(controls_frame, text="Sort", command=sort_numbers)
sort_button.pack(fill="x", pady=5)
clear_button = tk.Button(controls_frame, text="Clear All", command=clear_all)
clear_button.pack(fill="x", pady=5)

# Output Text Area
output_frame = tk.Frame(root, padx=10, pady=10)
output_frame.grid(row=0, column=2, sticky="nsew")
tk.Label(output_frame, text="Sorted Output:", anchor="w").pack(fill="x")
output_text_box = tk.Text(output_frame, height=20, width=40)
output_text_box.pack(fill="both", expand=True)

root.mainloop()
