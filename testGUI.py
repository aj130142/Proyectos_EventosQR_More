import tkinter as tk

def agregar_boton():
    # Crear un nuevo botón y agregarlo al frame interior
    imagen = tk.PhotoImage(width=50, height=50)
    nuevo_boton = tk.Button(
        frame_interior,
        text=f"Hola {contador[0] + 1}",
        image=imagen,
        compound="center",
        width=50,
        command=lambda n=contador[0]: print(f"Botón {n + 1} clickeado")
    )
    nuevo_boton.imagen = imagen 
    nuevo_boton.pack(pady=10, anchor="w")

    contador[0] += 1  # Actualizar contador
    actualizar_scrollregion()



def actualizar_scrollregion():
    # Actualizar el área de desplazamiento
    canvas.configure(scrollregion=canvas.bbox("all"))

def open_new_frame():
    new_frame = tk.Toplevel(ventana)
    new_frame.title("New Frame")

    new_frame.transient(ventana)
    #new_frame.protocol("WM_DELETE_WINDOW", ventana.destroy)
    new_frame.configure(takefocus=True)
    new_frame.grab_set()
    # Add widgets to the new frame as needed
    label = tk.Label(new_frame, text="This is a new frame")
    label.pack(padx=20, pady=20,side="left")

def cargar_botones():
    
    for _ in range(5):
        agregar_boton()
        
def auto_btn():
    btn_agregar = tk.Button(
    frame_controles,
    text="➕ Agregar Botón",
    command=agregar_boton,
    bg="lightblue",
    fg="black"
    )
    btn_agregar.pack()
# Configuración inicial
ventana = tk.Tk()
ventana.title("Botones Dinámicos con Scroll")
ventana.geometry("400x500")

open_new_frame()

# Contador para los botones (usamos lista para modificación en closure)
contador = [0]


# Frame para controles (botón de agregar)
frame_controles = tk.Frame(ventana)
frame_controles.pack(pady=10)

# Botón para agregar nuevos botones


# Canvas y Scrollbar
canvas = tk.Canvas(ventana, bg="white")
scrollbar = tk.Scrollbar(ventana, orient=tk.VERTICAL, command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)


# Empaquetado
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


# Frame interior para los botones
frame_interior = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame_interior, anchor="nw")

# Configurar actualización automática del scroll
frame_interior.bind("<Configure>", lambda e: actualizar_scrollregion())

# Agregar 5 botones iniciales
cargar_botones()
auto_btn()
ventana.mainloop()