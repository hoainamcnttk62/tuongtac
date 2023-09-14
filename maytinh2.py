import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def evaluate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Tạo cửa sổ
window = tk.Tk()
window.title("Máy tính casio")

# Tạo ô nhập
entry = tk.Entry(window, width=20, font=('Helvetica', 45))
entry.grid(row=0, column=0, columnspan=5)

# Tạo các nút số và phép toán
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    ('NGUYỄN HOÀI NAM', 4),  # Change to a tuple with the button text and columnspan
    '1', '2', '3', '*',
    '0', '.', '=', '/'
]

row_val = 2
col_val = 0

for button in buttons:
    if isinstance(button, tuple):  # If it's a tuple of buttons
        tk.Button(window, text=button[0], width=63, height=2, font=('Helvetica', 15),
                  command=lambda b=button[0]: button_click(b) if b != '=' else evaluate()).grid(row=row_val, column=col_val, columnspan=button[1])
    else:
        tk.Button(window, text=button, width=15, height=2, font=('Helvetica', 15),
                  command=lambda b=button: button_click(b) if b != '=' else evaluate()).grid(row=row_val, column=col_val)

    col_val += button[1] if isinstance(button, tuple) else 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Nút xóa
tk.Button(window, text="C", width=15, height=2, font=('Helvetica', 15), command=clear).grid(row=row_val, column=col_val)

# Hiển thị cửa sổ
window.mainloop()