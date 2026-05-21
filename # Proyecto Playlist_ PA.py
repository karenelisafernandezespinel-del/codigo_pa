# Proyecto Playlist_ PA
# PROGRAMA: PLAYLIST ENTRE AMIGOS - SPOTIFY

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

def calcular_duracion(lista):                    # Función con parámetro

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

