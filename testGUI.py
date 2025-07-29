import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.valor_actual = None
        
        boton = tk.Button(root, text="Guardar 42")
        boton.numero = 42
        boton.bind("<Button-1>", self.manejar_presion)
        boton.pack(pady=20)
        
        boton1 = tk.Button(root, text="Guardar 42")
        boton1.numero = 32
        boton1.bind("<Button-1>", self.manejar_presion)
        boton1.pack(pady=20)
        
        # Etiqueta para mostrar el valor
        self.etiqueta = tk.Label(root, text="Presiona un botón")
        self.etiqueta.pack()

    def manejar_presion(self, event):
        # Recuperar y almacenar el valor
        self.valor_actual = event.widget.numero
        
        # Actualizar interfaz
        self.etiqueta.config(text=f"Valor: {self.valor_actual}")
        
        # También puedes pasar el valor a otras funciones
        self.procesar_valor(self.valor_actual)
    
    def procesar_valor(self, numero):
        print(f"Procesando valor: {self.valor_actual * 2}")

root = tk.Tk()
app = App(root)
root.mainloop()