import tkinter as tk
from time import strftime
from tkcalendar import Calendar

def button_clicked():
    print("Button clicked!")

# Crear la ventana principal
root = tk.Tk()
root.title("Calendario en Tkinter")

button = tk.Button(root, 
                   text="Click Me", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="gray",
                   highlightcolor="red",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)

# Ejecutar la aplicación
root.mainloop()
