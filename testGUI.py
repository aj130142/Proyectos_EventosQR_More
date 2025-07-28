import tkinter as tk

def mostrar_seleccion(opcion):
    etiqueta.config(text=f"Seleccionaste: {opcion}")

ventana = tk.Tk()
ventana.title("Menú de Opciones")
ventana.geometry("600x600")

opciones = ["Opción 1", "Opción 2", "Opción 3"]
variable_seleccionada = tk.StringVar(ventana)
variable_seleccionada.set(opciones[0])  # Establecer un valor inicial

menu_opciones = tk.OptionMenu(ventana, variable_seleccionada, *opciones, command=mostrar_seleccion)
menu_opciones.pack(pady=100)

etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

ventana.mainloop()