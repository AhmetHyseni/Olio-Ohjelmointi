import tkinter as tk

width = 0

def change_width():
    global width
    width = width_slider.get()
    width_button.config(width=width)

def change_color():
    color = color_var.get()
    if color == 'red':
        color_button.config(bg='red')
    elif color == 'green':
        color_button.config(bg='green')
    elif color == 'blue':
        color_button.config(bg='blue')

def change_width_and_color(event=None):
    change_width()
    change_color()

root = tk.Tk()
root.geometry("700x400")

top_frame = tk.Frame(root)
top_frame.pack(side='top', fill='both', expand=True)

left_frame = tk.Frame(top_frame, width=350, height=200)
left_frame.pack(side='left', padx=20, pady=20, fill='both', expand=True)
left_frame.pack_propagate(0)

right_frame = tk.Frame(top_frame, width=350, height=200)
right_frame.pack(side='right', padx=20, pady=20, fill='both', expand=True)
right_frame.pack_propagate(0)

width_slider = tk.Scale(left_frame, from_=10, to=50, length=300, orient='horizontal')
width_slider.set(0)
width_slider.pack(side='top', pady=10)

color_var = tk.StringVar(value='red')
color_menu = tk.OptionMenu(right_frame, color_var, 'red', 'green', 'blue')
color_menu.pack(side='top', pady=10)

width_button = tk.Button(left_frame, text='Change Width', font=('Arial', 20), command=change_width)
width_button.pack(side='bottom', fill='both', expand=True)

color_button = tk.Button(right_frame, text='Change Color', font=('Arial', 20), command=change_color)
color_button.pack(side='bottom', fill='both', expand=True)

root.bind('<Return>', change_width_and_color)

root.mainloop()
