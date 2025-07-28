funciones_con_args = []

listaNombre=["¡Hola", "¿Qué tal?", "Adiós"]

def saludar(nombre, tono):
    return f"{tono} {nombre}!"

for tono in listaNombre:
    # Guardar solo la función con el tono preconfigurado
    funciones_con_args.append(lambda nombre, t=tono: saludar(nombre, t))

# Llamar a las funciones
print(funciones_con_args[0]("Sofía"))  # ¡Hola Sofía!
print(funciones_con_args[1]("David"))  # ¿Qué tal? David!