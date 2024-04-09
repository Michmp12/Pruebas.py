import os

# Función para limpiar la pantalla
def limpiar_pantalla():
    # Detecta el sistema operativo
    if os.name == 'nt':  # Windows
        _ = os.system('cls')
    else:  # Linux/Unix/MacOS
        _ = os.system('clear')

# Función para limpiar la pantalla antes de mostrar el menú principal de registro
def limpiar_menu():
    limpiar_pantalla()
    print("\n ---MENU PRINCIPAL DE REGISTRO --- :")

# Resto del código
registro_despachos = {}
numero_despacho = 1

def registrar_salida():
    global numero_despacho
    try:
        # Preguntas basicas  
        placa_vehiculo = input("Ingrese la Placa del vehiculo: ")
        descripcion_vehiculo = input("Ingrese la Placa de descripcion del vehiculo: ")
        nombre_conductor = input("Ingrese el Nombre del conductor: ")
        contacto_conductor = input("Ingrese el Contacto del conductor: ")
        ruta = input("Ingrese la Ruta: ")
        carga = input("Ingrese la Descripcion de la carga: ")

        despacho = {
            "Placa del vehiculo": placa_vehiculo,
            "Placa de descripcion del vehiculo": descripcion_vehiculo,
            "Nombre del conductor": nombre_conductor,
            "Contacto del conductor": contacto_conductor,
            "Ruta": ruta,
            "Carga": carga
        }
        #Recomendacion de boxblack
        registro_despachos[numero_despacho] = despacho
        numero_despacho += 1
        print("Registro de salida exitoso.")
    except Exception as e:
        print("Ha ocurrido un error:", e)

def mostrar_salidas():
    limpiar_pantalla()  # Limpia la pantalla antes de mostrar las salidas
    print("--- REGISTRO DE SALIDA ---")
    if registro_despachos:
        for numero_despacho, despacho in registro_despachos.items():
            print(f"Número de Despacho: {numero_despacho}")
            for clave, valor in despacho.items():
                print(f"{clave}: {valor}")
            print("--------------------------")
    else:
        print("No hay registros de salida.")

# Menú principal para que le pregunte al usuario cuando quiera ingresar o ver las salidas :P
while True:
    limpiar_menu()  # Limpia la pantalla antes de mostrar el menú principal
    print("1. Registro de salida")
    print("2. Mostrar salidas")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_salida()
    elif opcion == "2":
        mostrar_salidas()
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción que si sea válida para hacer el registro.")
