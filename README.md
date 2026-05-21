#Proyecto Playlist_ PA
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
