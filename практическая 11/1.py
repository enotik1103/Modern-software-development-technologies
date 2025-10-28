import tkinter as tk
from tkinter import ttk, filedialog, messagebox
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Голев Дмитрий Юрьевич") 
        self.geometry("800x600") 
        self.create_tabs()  
        self.resizable(False, False)  
    def create_tabs(self):
        tab_control = ttk.Notebook(self)
        calculator_tab = ttk.Frame(tab_control)
        tab_control.add(calculator_tab, text="Калькулятор")
        self.create_calculator(calculator_tab)
        checkbox_tab = ttk.Frame(tab_control)
        tab_control.add(checkbox_tab, text="Выбор варианта")
        self.create_checkboxes(checkbox_tab)
        text_tab = ttk.Frame(tab_control)
        tab_control.add(text_tab, text="Работа с текстом")
        self.create_text_widget(text_tab)
        tab_control.pack(expand=True, fill="both")
    def create_calculator(self, parent):
        frame = ttk.LabelFrame(parent, text="Калькулятор", padding=(15))
        frame.grid(column=0, row=0, sticky="nwes")
        lbl_num1 = ttk.Label(frame, text="Первое число:")
        lbl_num1.grid(column=0, row=0, padx=5, pady=5)
        entry_num1 = ttk.Entry(frame)
        entry_num1.grid(column=1, row=0, padx=5, pady=5)
        lbl_num2 = ttk.Label(frame, text="Второе число:")
        lbl_num2.grid(column=0, row=1, padx=5, pady=5)
        entry_num2 = ttk.Entry(frame)
        entry_num2.grid(column=1, row=1, padx=5, pady=5)
        operation = tk.StringVar(value="+")
        combo_operation = ttk.Combobox(frame, values=["+", "-", "*", "/"], state="readonly", textvariable=operation)
        combo_operation.grid(column=0, row=2, columnspan=2, padx=5, pady=5)
        btn_calc = ttk.Button(frame, text="Результат", command=lambda: self.calculate(entry_num1.get(), entry_num2.get(), operation.get()))
        btn_calc.grid(column=0, row=3, columnspan=2, padx=5, pady=5)
        self.result_label = ttk.Label(frame, text="", font=("Arial", 14))
        self.result_label.grid(column=0, row=4, columnspan=2, padx=5, pady=5)
    def calculate(self, num1, num2, op):
        try:
            a = float(num1)
            b = float(num2)
            if op == "+":
                res = a + b
            elif op == "-":
                res = a - b
            elif op == "*":
                res = a * b
            elif op == "/" and b != 0:
                res = a / b
            else:
                res = "Деление на ноль невозможно!"
            self.result_label.config(text=f"Результат: {res}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")
    def create_checkboxes(self, parent):
        frame = ttk.LabelFrame(parent, text="Выбор варианта", padding=(10))
        frame.grid(column=0, row=0, sticky="nwes")
        self.check_var1 = tk.IntVar()
        chk_box1 = ttk.Checkbutton(frame, text="Первый вариант", variable=self.check_var1)
        chk_box1.grid(column=0, row=0, padx=5, pady=5)
        self.check_var2 = tk.IntVar()
        chk_box2 = ttk.Checkbutton(frame, text="Второй вариант", variable=self.check_var2)
        chk_box2.grid(column=0, row=1, padx=5, pady=5)
        self.check_var3 = tk.IntVar()
        chk_box3 = ttk.Checkbutton(frame, text="Третий варинат", variable=self.check_var3)
        chk_box3.grid(column=0, row=2, padx=5, pady=5)
        btn_select = ttk.Button(frame, text="Подтвердить выбор", command=self.on_checkbox_click)
        btn_select.grid(column=0, row=3, padx=5, pady=5)
    def on_checkbox_click(self):
        selected = []
        if self.check_var1.get():
            selected.append("Первый вариант")
        if self.check_var2.get():
            selected.append("Второй вариант")
        if self.check_var3.get():
            selected.append("Третий вариант")
        if selected:
            messagebox.showinfo("Выбор сделан", f"Вы выбрали варианты: {' '.join(selected)}")
        else:
            messagebox.showwarning("Предупреждение", "Нет выбранных вариантов")
    def create_text_widget(self, parent):
        frame = ttk.LabelFrame(parent, text="Работа с текстом", padding=(10))
        frame.grid(column=0, row=0, sticky="nwes")
        self.text_area = tk.Text(frame, height=10, width=50)
        self.text_area.grid(column=0, row=0, padx=5, pady=5)
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=False)
        file_menu.add_command(label="Загрузить файл", command=self.load_file)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        self.config(menu=menu_bar)
    def load_file(self):
        filename = filedialog.askopenfilename(title="Выберите файл", filetypes=[("Text files", "*.txt"), ("All Files", "*.*")])
        if filename:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
if __name__ == "__main__":
    app = Application()
    app.mainloop()