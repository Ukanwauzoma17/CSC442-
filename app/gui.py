import tkinter as tk
from tkinter import messagebox

def calculate_actual_size(specimen_size, magnification):
    return specimen_size * magnification

def calculate_size():
    username = username_entry.get()
    specimen_size = float(specimen_size_entry.get())
    magnification = float(magnification_entry.get())
    
    actual_size = calculate_actual_size(specimen_size, magnification)
    messagebox.showinfo("Result", f"Actual size: {actual_size} mm")

app = tk.Tk()
app.title("Microscope Size Calculator")

tk.Label(app, text="Username").pack()
username_entry = tk.Entry(app)
username_entry.pack()

tk.Label(app, text="Specimen Size (mm)").pack()
specimen_size_entry = tk.Entry(app)
specimen_size_entry.pack()

tk.Label(app, text="Magnification").pack()
magnification_entry = tk.Entry(app)
magnification_entry.pack()

tk.Button(app, text="Calculate", command=calculate_size).pack()

app.mainloop()