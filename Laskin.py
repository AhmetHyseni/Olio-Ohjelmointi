import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Laskin")
        master.geometry("300x400")
        
        # Luo syötteen ja tulosteen tekstikentät
        self.input_entry = tk.Entry(master)
        self.input_entry.pack()
        
        self.output_label = tk.Label(master, text="0")
        self.output_label.pack()
        
        # Luo nappi yhteenlaskua varten
        self.add_button = tk.Button(master, text="+", command=self.add_numbers)
        self.add_button.pack()
        
        # Luo nappi vähennyslaskua varten
        self.subtract_button = tk.Button(master, text="-", command=self.subtract_numbers)
        self.subtract_button.pack()
        
        # Luo nappi kertolaskua varten
        self.multiply_button = tk.Button(master, text="*", command=self.multiply_numbers)
        self.multiply_button.pack()
        
        # Luo nappi jakolaskua varten
        self.divide_button = tk.Button(master, text="/", command=self.divide_numbers)
        self.divide_button.pack()
        
    def add_numbers(self):
        try:
            num1 = float(self.input_entry.get())
            num2 = float(self.output_label.cget("text"))
            result = num1 + num2
            self.output_label.configure(text=str(result))
        except ValueError:
            pass
        
    def subtract_numbers(self):
        try:
            num1 = float(self.input_entry.get())
            num2 = float(self.output_label.cget("text"))
            result = num2 - num1
            self.output_label.configure(text=str(result))
        except ValueError:
            pass
        
    def multiply_numbers(self):
        try:
            num1 = float(self.input_entry.get())
            num2 = float(self.output_label.cget("text"))
            result = num1 * num2
            self.output_label.configure(text=str(result))
        except ValueError:
            pass
        
    def divide_numbers(self):
        try:
            num1 = float(self.input_entry.get())
            num2 = float(self.output_label.cget("text"))
            result = num2 / num1
            self.output_label.configure(text=str(result))
        except ValueError:
            pass

window = tk.Tk()
app = CalculatorApp(window)
window.mainloop()
