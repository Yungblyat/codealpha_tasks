import tkinter as tk

def generate_fibonacci():
    try:
        n = int(entry.get())
        if n <= 0:
            result_label.config(text="Please enter a positive integer.")
            return
        fibonacci_numbers = []
        a, b = 0, 1
        for _ in range(n+1):  # Adjusted to iterate n+1 times
            fibonacci_numbers.append(a)
            a, b = b, a + b
        result_label.config(text="Fibonacci numbers: " + ", ".join(map(str, fibonacci_numbers[1:])))
    except ValueError:
        result_label.config(text="Invalid input. Please enter a positive integer.")

# window
window = tk.Tk()
window.title("Fibonacci Generator")

#  widgets
label = tk.Label(window, text="Enter the number of Fibonacci numbers to generate:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

generate_button = tk.Button(window, text="Generate Fibonacci Numbers", command=generate_fibonacci)
generate_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()


window.mainloop()
