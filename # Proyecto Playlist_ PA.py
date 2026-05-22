# Proyecto Playlist_ PA
# PROGRAMA: PLAYLIST ENTRE AMIGOS - SPOTIFY
# REALIZADO POR:
     # Danna Valentina Saavedra Morales
     # Karen Elisa Fernandez Espinel
     # Danna Camila Gonzales Gutiérrez
     # Miguel Ángel Piragauta Sanchez
     # Paula Andrea Castañeda Quintero

# ---------------- LIBRERÍAS ----------------

import random                 # Librería para números aleatorios
import math                   # Librería matemática
import datetime               # Librería para fechas

# ---------------- LISTA PRINCIPAL ----------------

playlist = []                 # Lista donde se guardan canciones


# ======================================================
# FUNCIÓN VOID
# Muestra el menú
# ======================================================

def mostrar_menu():                                     # Función menú
    print("\n======= PLAYLIST SPOTIFY =======")   # Título
    print("1. Agregar canción")                  # Opción 1
    print("2. Mostrar playlist")                 # Opción 2
    print("3. Buscar canción")                   # Opción 3
    print("4. Ver estadísticas")                 # Opción 4
    print("5. Salir")                            # Opción 5

# ======================================================
# FUNCIÓN CON RETURN
# Retorna duración total
# ======================================================

def calcular_duracion():                    # Función con parámetro

    total = 0                                    # Variable acumuladora

    # Big O = O(n)
    # Recorre toda la lista
    for cancion in lista:                        # Ciclo for
        total += cancion["duracion"]             # Suma duración
    return total                                 # Retorna total

# ======================================================
# FUNCIÓN PARA AGREGAR CANCIÓN
# ======================================================

def agregar_cancion():                           # Función agregar

    try:                                         # Intenta ejecutar
        nombre = input("Ingrese nombre canción: ")   # Pide nombre
        artista = input("Ingrese artista: ")         # Pide artista
        amigo = input("¿Qué amigo la agregó?: ")     # Pide amigo
        duracion = int(input("Ingrese duración: "))  # Pide duración
        codigo = random.randint(1000, 9999)          # Genera código
        fecha = datetime.datetime.now()              # Fecha actual

        cancion = {                                  # Diccionario canción
            "codigo": codigo,                        # Guarda código
            "nombre": nombre,                        # Guarda nombre
            "artista": artista,                      # Guarda artista
            "amigo": amigo,                          # Guarda amigo
            "duracion": duracion,                    # Guarda duración
            "fecha": fecha                           # Guarda fecha
        }

        playlist.append(cancion)                     # Agrega canción

        print("Canción agregada correctamente")      # Mensaje
        print("Código:", codigo)                     # Muestra código

    except ValueError:                               # Error si escribe texto
        print("Error: la duración debe ser un número")
# ======================================================
# FUNCIÓN PARA MOSTRAR PLAYLIST
# ======================================================

def mostrar_playlist():                              # Función mostrar

    if len(playlist) == 0:                           # Verifica lista vacía
        print("La playlist está vacía")              # Mensaje

    else:                                            # Si hay canciones

        print("\n===== PLAYLIST =====")              # Título

        # Big O = O(n)
        for cancion in playlist:                     # Recorre lista
            print("----------------------")     # Línea
            print("Código:", cancion["codigo"])      # Código
            print("Canción:", cancion["nombre"])     # Nombre
            print("Artista:", cancion["artista"])    # Artista
            print("Agregada por:", cancion["amigo"]) # Amigo
            print("Duración:", cancion["duracion"])  # Duración
            print("Fecha:", cancion["fecha"])        # Fecha


# ======================================================
# FUNCIÓN PARA BUSCAR CANCIÓN
# ======================================================

def buscar_cancion():                                # Función buscar

    try:                                             # Intenta ejecutar

        codigo_buscar = int(input("Ingrese código: ")) # Pide código
        encontrado = False                           # Variable lógica

        # Big O = O(n)
        for cancion in playlist:                     # Recorre lista

            if cancion["codigo"] == codigo_buscar:   # Compara código

                print("\nCanción encontrada")       # Mensaje
                print("Nombre:", cancion["nombre"])  # Nombre
                print("Artista:", cancion["artista"]) # Artista
                print("Agregada por:", cancion["amigo"]) # Amigo

                encontrado = True                    # Cambia variable
                break                                # Rompe ciclo

        if encontrado == False:                      # Si no encuentra
            print("Canción no encontrada")           # Mensaje

    except ValueError:                               # Error si escribe letras

        print("Error: debe ingresar un número")

# ======================================================
# FUNCIÓN ESTADÍSTICAS
# ======================================================

def estadisticas(lista):                                  # Función estadísticas

    cantidad = len(playlist)                         # Cuenta canciones
    total = calcular_duracion(playlist)              # Llama función

    print("Cantidad de canciones:", cantidad)        # Muestra cantidad
    print("Duración total:", total)                  # Muestra total

    if cantidad > 0:                                 # Verifica cantidad
        promedio = total / cantidad                  # Calcula promedio
        print("Promedio:", promedio)                 # Muestra promedio
        raiz = math.sqrt(promedio)                   # Calcula raíz
        print("Raíz del promedio:", raiz)            # Muestra raíz

        if promedio >= 300:                          # Condición
            print("Playlist con canciones de duración larga")   # Mensaje

        elif promedio >= 180:                        # Otra condición
            print("Playlist con canciones de duración media") # Mensaje

        else:                                        # Si no cumple
            print("Playlist con canciones de duración corta")   # Mensaje

    else:                                            # Si no hay canciones
        print("No hay canciones registradas")        # Mensaje
        
# ======================================================
# FUNCIÓN MAIN
# Función principal del programa
# ======================================================

def main():                                          # Función principal

    opcion = 0                                       # Variable opción

    # Ciclo while
    while opcion != 5:                               # Mientras no sea 5
        mostrar_menu()                               # Llama menú

        try:                                         # Intenta ejecutar

            opcion = int(input("Seleccione opción: ")) # Pide opción

            # MATCH CASE
            match opcion:                            # Evalúa opción

                case 1:                              # Caso 1
                    agregar_cancion()                # Llama función

                case 2:                              # Caso 2
                    mostrar_playlist()               # Llama función

                case 3:                              # Caso 3
                    buscar_cancion()                # Llama función

                case 4:                              # Caso 4
                    estadisticas()                   # Llama función

                case 5:                              # Caso 5
                    print("Cerrando Spotify...")     # Mensaje

                case _:                              # Caso por defecto
                    print("Opción incorrecta")       # Mensaje

        except ValueError:                           # Captura error

            print("Error: debe ingresar números")

# ======================================================
# LLAMADO DE LA FUNCIÓN MAIN
# ======================================================

main()                                               # Ejecuta programa


