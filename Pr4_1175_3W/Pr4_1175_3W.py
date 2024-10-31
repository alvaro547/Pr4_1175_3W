print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Inicializamos un diccionario para almacenar la información personal
informacion_personal = {}

# Pedimos al usuario que ingrese su información
informacion_personal['nombre'] = input("Ingrese su nombre: ")
informacion_personal['edad'] = int(input("Ingrese su edad: "))
informacion_personal['direccion'] = input("Ingrese su dirección: ")
informacion_personal['telefono'] = input("Ingrese su número de teléfono: ")

# Mostramos la información ingresada
print(f"{informacion_personal['nombre']} tiene {informacion_personal['edad']} años, "
      f"vive en {informacion_personal['direccion']} y su número de teléfono es {informacion_personal['telefono']}.")
