import tkinter as tk

class MiApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Inicializar la clase padre (tk.Tk)
        contador=[0]
        # Configuración inicial de la ventana
        self.title("Botones Dinámicos con Scroll")          # Título
        self.geometry("600x600")       # Tamaño (ancho x alto)
        self.resizable(True, False)     # Permitir redimensionar (ancho, alto)
        self.contador= contador
        #otra parte del codigo
        self.crear_PrincipalFrame()
        self.agregar_boton()
        self.cargar_botones()
        self.auto_btn()
        self.open_new_frame()
        
        # Llamar a métodos de inicialización
        #self.contador[0]()
        


    def crear_PrincipalFrame(self): #metodo para crear los inicializar los canvas, scrollbar, etc.
        self.frame_principal = tk.Frame(self, bg="#f0f0f0")
        self.frame_principal.pack(fill="both", expand=True, padx=20, pady=20)
        self.frame_controles = tk.Frame(self.frame_principal)
        self.frame_controles.pack(pady=10)
        self.canvas = tk.Canvas(self.frame_principal, bg="white")
        self.scrollbar = tk.Scrollbar(self.frame_principal, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Empaquetado
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Frame interior para los botones
        self.frame_interior = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_interior, anchor="nw")

        # Configurar actualización automática del scroll
        self.frame_interior.bind("<Configure>", lambda e: self.actualizar_scrollregion())

    def agregar_boton(self):
        # Crear un nuevo botón y agregarlo al frame interior
        self.imagen = tk.PhotoImage(width=50, height=50)
        self.nuevo_boton = tk.Button(
            self.frame_interior,
            text=f"Hola {self.contador[0] + 1}",
            image=self.imagen,
            compound="center",
            width=50,
            command=lambda n=self.contador[0]: print(f"Botón {n + 1} clickeado")
        )
        self.nuevo_boton.imagen = self.imagen 
        self.nuevo_boton.pack(pady=10, anchor="w")

        self.contador[0] += 1  # Actualizar contador
        self.actualizar_scrollregion()

    def actualizar_scrollregion(self):
    # Actualizar el área de desplazamiento
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def cargar_botones(self):
        
        for _ in range(5):
            self.agregar_boton()
            
    def auto_btn(self):
        self.btn_agregar = tk.Button(
        self.frame_controles,
        text="➕ Agregar Botón",
        command=self.agregar_boton,
        bg="lightblue",
        fg="black"
        )
        self.btn_agregar.pack()
    def open_new_frame(self):
        self.new_frame = tk.Toplevel(self.frame_principal)
        self.new_frame.title("New Frame")

        self.new_frame.transient(self.frame_principal)
        self.new_frame.protocol("WM_DELETE_WINDOW", self.destroy)
        self.new_frame.configure(takefocus=True)
        self.new_frame.grab_set()
        # Add widgets to the new frame as needed
        self.label = tk.Label(self.new_frame, text="This is a new frame")
        self.label.pack(padx=20, pady=20,side="left")
    def iniciar(self):
        self.vista.mainloop()

if __name__ == "__main__":
    app = MiApp()    # Instanciar la aplicación
    
    app.mainloop()   # Ejecutar el bucle principal
