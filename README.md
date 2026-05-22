================================================================
     EXPLICACIÓN COMPLETA DEL CÓDIGO
     ARCHIVO: playlist_PA.py
     PROGRAMA: PLAYLIST ENTRE AMIGOS - SPOTIFY
================================================================
     REALIZADO POR:
      → Danna Valentina Saavedra Morales
      → Karen Elisa Fernandez Espinel
      → Danna Camila Gonzales Gutiérrez
      → Miguel Ángel Piragauta Sanchez
      → Paula Andrea Castañeda Quintero
================================================================


Este documento explica, línea por línea y sección por sección,
todo el código del programa. 

================================================================
SECCIÓN 1: ENCABEZADO DEL PROGRAMA
================================================================

# PROGRAMA: PLAYLIST ENTRE AMIGOS - SPOTIFY

  - Esta línea es un COMENTARIO. 
  - Su función es DOCUMENTAR: cual es el nombre y propósito general
    del programa.
 - El programa simula una lista de reproducción (playlist) al
    estilo Spotify, donde varios amigos pueden agregar canciones,
    buscarlas y ver estadísticas.


================================================================
SECCIÓN 2: LIBRERÍAS IMPORTADAS
================================================================

¿Qué es una librería?
  Una librería es un conjunto de herramientas (funciones y
  utilidades) ya construidas por Python que podemos "pedir
  prestadas" para usar en nuestro programa. 

  La palabra clave para importarlas es: import

--------------------------------------------------------------
2.1  import random
--------------------------------------------------------------

  - Importa la librería "random" de Python.
  - Esta librería permite generar números ALEATORIOS,
    es decir, valores al azar dentro de un rango definido.
  - En este programa se usa específicamente para:
      * Generar automáticamente un CÓDIGO ÚNICO para cada
        canción que se agrega a la playlist.

 Función usada en el programa:
      codigo = random.randint(1000, 9999)

Explicación detallada:
      - En este caso genera un número entre 1000 y 9999,
        lo que da exactamente 4 dígitos.
      - Cada vez que se agrega una canción, se genera un código
        diferente de forma automática, sin que el usuario
        tenga que escribirlo.
      - Ese código queda guardado en el diccionario de la
        canción como identificador único.

 --------------------------------------------------------------
2.2  import math
--------------------------------------------------------------

  - Importa la librería "math" de Python.
  - Esta librería contiene operaciones MATEMÁTICAS avanzadas
    que no están disponibles de forma directa en Python básico.
 - En este programa se usa específicamente para:
      * Calcular la RAÍZ CUADRADA del promedio de duración
        de las canciones en la playlist.

  Función usada en el programa:
      math.sqrt(promedio)

  Explicación detallada:
      - math.sqrt(x) calcula la raíz cuadrada de un número x.
      - Primero se calcula el promedio de duración de todas
        las canciones (suma de duraciones dividida entre el
        número total de canciones).
      - Este valor le da al programa una medida estadística
        adicional sobre los tiempos de las canciones.

--------------------------------------------------------------
2.3  import datetime
--------------------------------------------------------------

  - Importa la librería "datetime" de Python.
  - Esta librería permite trabajar con FECHAS Y HORAS.
   con precisión exacta.
  - En este programa se usa específicamente para:
      * Registrar el momento EXACTO en que una canción
        fue agregada a la playlist (día, mes, año, hora,
        minutos y segundos).

  Función usada en el programa:
      fecha = datetime.datetime.now()

  Explicación detallada:
      - datetime.datetime.now() captura la fecha y hora
        exacta del sistema en el momento en que se ejecuta.
      - Ese valor queda guardado en la variable "fecha" y
        se almacena dentro del diccionario de la canción.
      - Es útil para ordenar canciones por fecha de registro
        o para mostrar el historial de la playlist.


================================================================
SECCIÓN 3: LISTA PRINCIPAL (VARIABLE GLOBAL)
================================================================

playlist = []

--------------------------------------------------------------
¿Qué es esta línea?
--------------------------------------------------------------

  - Se declara una variable llamada "playlist".
  - Se inicializa como una LISTA VACÍA [ ].
  - Una lista en Python es una colección de elementos que puede
    crecer o reducirse.

--------------------------------------------------------------
¿Por qué es GLOBAL?
--------------------------------------------------------------

  - Esta variable se declara FUERA de cualquier función.
  - Eso significa que TODAS las funciones del programa pueden
    verla y modificarla.
  - Es el "almacén central" donde viven todas las canciones
    del programa.

--------------------------------------------------------------
¿Qué guarda esta lista?
--------------------------------------------------------------

  - Cada canción se guarda como un DICCIONARIO dentro de la lista.
  - Un diccionario almacena información en pares clave:valor.

  Ejemplo de cómo se vería la lista con datos:

      playlist = [
          {
              "titulo"  : "Luna",
              "artista" : "Feid",
              "duracion": 197
          },
          {
              "titulo"  : "El Beneficio de la Duda",
              "artista" : "Grupo firme",
              "duracion": 252
          }
      ]

  - "titulo"   → nombre de la canción (texto / string)
  - "artista"  → nombre del artista   (texto / string)
  - "duracion" → duración en segundos (número entero / int)


================================================================
SECCIÓN 4: FUNCIÓN mostrar_menu()
================================================================

  TIPO DE FUNCIÓN : VOID (no retorna ningún valor)
  PARÁMETROS      : Ninguno
  RETORNA         : Nada (None)

--------------------------------------------------------------
Código completo de la función:
--------------------------------------------------------------

    def mostrar_menu():
        print("\n======= PLAYLIST SPOTIFY =======")
        print("1. Agregar canción")
        print("2. Mostrar playlist")
        print("3. Buscar canción")
        print("4. Ver estadísticas")
        print("5. Salir")

--------------------------------------------------------------
Explicación línea por línea:
--------------------------------------------------------------

  def mostrar_menu():
  → La palabra "def" indica que se está DEFINIENDO una función.
  → "mostrar_menu" es el nombre que le damos a esta función.
  → Los paréntesis () vacíos indican que no recibe parámetros.

  print("\n======= PLAYLIST SPOTIFY =======")
  → Imprime el TÍTULO del menú en pantalla.
  → El "\n" al inicio es un salto de línea: deja una línea en
    blanco antes del título para que el menú se vea más limpio.
  → Los signos "=======" son decorativos, para enmarcar el título.

  print("1. Agregar canción")
  → Imprime la opción número 1 del menú.
  → Al elegirla, el usuario podrá ingresar una nueva canción
    a la playlist.

  print("2. Mostrar playlist")
  → Imprime la opción número 2 del menú.
  → Al elegirla, se mostrará la lista completa de canciones
    que han sido agregadas.

  print("3. Buscar canción")
  → Imprime la opción número 3 del menú.
  → Al elegirla, el usuario podrá buscar una canción específica
    por su título, artista u otro campo.

  print("4. Ver estadísticas")
  → Imprime la opción número 4 del menú.
  → Al elegirla, se muestran datos generales de la playlist,
    como la duración total de todas las canciones o el número
    total de canciones guardadas.

  print("5. Salir")
  → Imprime la opción número 5 del menú.
  → Al elegirla, el programa termina su ejecución de forma
    ordenada.


================================================================
SECCIÓN 5: FUNCIÓN calcular_duracion(lista)
================================================================

  TIPO DE FUNCIÓN : CON RETURN (retorna un valor)
  PARÁMETROS      : lista → recibe una lista de canciones
  RETORNA         : total → número con la suma de duraciones

--------------------------------------------------------------
Código completo de la función:
--------------------------------------------------------------

    def calcular_duracion(lista):
        total = 0
        for cancion in lista:
            total += cancion["duracion"]
        return total

--------------------------------------------------------------
Explicación línea por línea:
--------------------------------------------------------------

  def calcular_duracion(lista):
  → Se define la función con el nombre "calcular_duracion".
  → Recibe UN parámetro llamado "lista".
  → Este parámetro es la lista de canciones sobre la que
    se hará el cálculo. Se le pasará la variable
    global "playlist".

  total = 0
  → Se crea una variable llamada "total" y se inicia en cero.
  → Esta es una VARIABLE ACUMULADORA: su trabajo es ir
    sumando valores a medida que el ciclo avanza.
  → Se debe iniciar en 0 para que la primera suma sea correcta.

  for cancion in lista:
  → Inicia un CICLO FOR que recorre la lista de canciones.
  → En cada vuelta (iteración), la variable "cancion" toma
    el valor de un elemento de la lista.
  → El ciclo se repite tantas veces como canciones haya en
    la lista.

  total += cancion["duracion"]
  → En cada iteración, se accede al valor de la clave "duracion"
    de la lista actual.
  → Ese valor se SUMA al acumulador "total".
  → El operador "+=" es un atajo que significa:
        total = total + cancion["duracion"]

  Ejemplo paso a paso con las 3 canciones anteriores:
      Antes del ciclo : total = 0
      Iteración 1     : total = 0   + 180 = 180
      Iteración 2     : total = 180 + 240 = 420
      Iteración 3     : total = 420 + 210 = 630
      Resultado final : total = 630

  return total
  → Al terminar el ciclo, la función RETORNA el valor de "total".
  → Quien llame a esta función recibirá ese número como resultado.

--------------------------------------------------------------
Complejidad Algorítmica: Big O = O(n)
--------------------------------------------------------------

  - La notación Big O describe qué tan eficiente es una función
    según el tamaño de sus datos de entrada.

  - En esta función, el ciclo "for" recorre TODA la lista
    una sola vez.

  - Si la lista tiene n canciones:
      * 10 canciones   → 10 iteraciones
      * 100 canciones  → 100 iteraciones
      * 1000 canciones → 1000 iteraciones

  - El tiempo de ejecución crece de forma LINEAL con n.
  - Por eso se dice que su complejidad es O(n):
    "a mayor cantidad de canciones, más tiempo, pero de forma
    proporcional y predecible".

  - O(n) es considerada una complejidad EFICIENTE para
    operaciones de recorrido de listas.

===============================================================
SECCIÓN 6: FUNCIÓN agregar_cancion()
================================================================

  TIPO DE FUNCIÓN : VOID (no retorna ningún valor)
  PARÁMETROS      : Ninguno
  RETORNA         : Nada
  USA try/except  : Sí, para capturar errores de tipo ValueError

--------------------------------------------------------------
Código completo de la función:
--------------------------------------------------------------

    def agregar_cancion():
        try:
            nombre   = input("Ingrese nombre canción: ")
            artista  = input("Ingrese artista: ")
            amigo    = input("¿Qué amigo la agregó?: ")
            duracion = int(input("Ingrese duración: "))
            codigo   = random.randint(1000, 9999)
            fecha    = datetime.datetime.now()

            cancion = {
                "codigo"  : codigo,
                "nombre"  : nombre,
                "artista" : artista,
                "amigo"   : amigo,
                "duracion": duracion,
                "fecha"   : fecha
            }

            playlist.append(cancion)
            print("Canción agregada correctamente")
            print("Código:", codigo)

        except ValueError:
            print("Error: la duración debe ser un número")

--------------------------------------------------------------
Explicación línea por línea:
--------------------------------------------------------------

  def agregar_cancion():
  → Se define la función con el nombre "agregar_cancion".
  → No recibe parámetros porque los datos los pide directamente
    al usuario con input().

  try:
  → Inicia el bloque de intento.
  → Le dice a Python: "intenta ejecutar todo lo que está
    aquí adentro".
  → Si algo falla, no rompe el programa sino que salta
    al bloque except.

  nombre = input("Ingrese nombre canción: ")
  → Muestra el mensaje en pantalla y espera que el usuario
    escriba el nombre de la canción.
  → Lo que el usuario escribe queda guardado en "nombre".
  → input() siempre retorna texto (string).

  artista = input("Ingrese artista: ")
  → Igual que el anterior, pero pide el nombre del artista.
  → Se guarda en la variable "artista".

  amigo = input("¿Qué amigo la agregó?: ")
  → Pide el nombre del amigo que está agregando la canción.
  → Se guarda en la variable "amigo".

  duracion = int(input("Ingrese duración: "))
  → Pide la duración de la canción en segundos.
  → input() devuelve texto, pero int() lo convierte a número.
  → AQUÍ puede ocurrir el error: si el usuario escribe letras
    en lugar de números, int() falla y se activa el except.
  → Se guarda en la variable "duracion".

  codigo = random.randint(1000, 9999)
  → Genera automáticamente un código de 4 dígitos al azar.
  → El usuario no lo escribe, el programa lo crea solo.
  → Sirve como identificador único de la canción.

  fecha = datetime.datetime.now()
  → Captura la fecha y hora exacta del momento en que
    se está agregando la canción.
  → Queda registrado cuándo fue ingresada.

  cancion = { ... }
  → Se crea un DICCIONARIO llamado "cancion" con todos
    los datos recopilados.
  → Un diccionario guarda información en pares clave:valor.
  → Las claves son: "codigo", "nombre", "artista", "amigo",
    "duracion", "fecha".
  → Los valores son las variables que se llenaron arriba.


  playlist.append(cancion)
  → append() es un método de las listas que agrega un elemento
    al FINAL de la lista.
  → En este caso agrega el diccionario "cancion" a la lista
    global "playlist".
  → Así la canción queda guardada en el programa.

  print("Canción agregada correctamente")
  → Muestra un mensaje de confirmación al usuario.

  print("Código:", codigo)
  → Muestra el código generado para que el usuario lo anote.
  → Ese código servirá después para buscar la canción.

  except ValueError:
  → Si en algún momento dentro del try ocurrió un error
    de tipo ValueError (por ejemplo, escribir "dos" en lugar
    de un número para la duración), el programa llega aquí.
  → En lugar de cerrarse con error, muestra un mensaje claro.

  print("Error: la duración debe ser un número")
  → Informa al usuario qué salió mal.


================================================================
SECCIÓN 7: FUNCIÓN mostrar_playlist(Lista)
================================================================

  TIPO DE FUNCIÓN : VOID (no retorna ningún valor)
  PARÁMETROS      : Lista
  RETORNA         : Nada
  COMPLEJIDAD     : O(n) — recorre toda la playlist

--------------------------------------------------------------
Código completo de la función:
--------------------------------------------------------------

    def mostrar_playlist(lista):
        if len(playlist) == 0:
            print("La playlist está vacía")
        else:
            print("\n===== PLAYLIST =====")
            for cancion in playlist:
                print("----------------------")
                print("Código:", cancion["codigo"])
                print("Canción:", cancion["nombre"])
                print("Artista:", cancion["artista"])
                print("Agregada por:", cancion["amigo"])
                print("Duración:", cancion["duracion"])
                print("Fecha:", cancion["fecha"])

--------------------------------------------------------------
Explicación línea por línea:
--------------------------------------------------------------

  def mostrar_playlist():
  → Se define la función. 
  → Recibe UN parámetro llamado "lista".
  → Este parámetro es la lista de canciones sobre la que
    se hará el cálculo. Se le pasará la variable
    global "playlist".

  if len(playlist) == 0:
  → len() es una función de Python que cuenta cuántos elementos
    tiene una lista.
  → Si len(playlist) es igual a 0, significa que no hay
    ninguna canción guardada todavía.
  → Esta verificación evita mostrar una lista vacía o generar
    un error al intentar recorrerla sin datos.

  print("La playlist está vacía")
  → Si no hay canciones, se informa al usuario con este mensaje
    y la función termina sin hacer nada más.

  else:
  → Si SÍ hay canciones (len > 0), se ejecuta este bloque.

  print("\n===== PLAYLIST =====")
  → Imprime el título decorativo de la sección.
  → El "\n" agrega una línea en blanco arriba para que
    se vea más ordenado en pantalla.

  for cancion in playlist:
  → Ciclo FOR que recorre CADA elemento de la lista playlist.
  → En cada vuelta, "cancion" representa un diccionario
    con los datos de una canción.
  → COMPLEJIDAD Big O = O(n): si hay 10 canciones se ejecuta
    10 veces, si hay 100 se ejecuta 100 veces.

  print("----------------------")
  → Imprime una línea separadora entre canciones para que
    la información se vea ordenada y clara.

  print("Código:", cancion["codigo"])
  → Accede al valor de la clave "codigo" del diccionario
    actual y lo muestra en pantalla.

  print("Canción:", cancion["nombre"])
  → Muestra el nombre de la canción.

  print("Artista:", cancion["artista"])
  → Muestra el nombre del artista.

  print("Agregada por:", cancion["amigo"])
  → Muestra el nombre del amigo que agregó la canción.

  print("Duración:", cancion["duracion"])
  → Muestra la duración en segundos.

  print("Fecha:", cancion["fecha"])
  → Muestra la fecha y hora exacta en que fue registrada.

  Ejemplo de salida en pantalla con una canción:

      ===== PLAYLIST =====
      ----------------------
      Código: 4827
      Canción: El Beneficio de la Duda
      Artista: Grupo firme
      Agregada por:  Valentina
      Duración: 252
      Fecha: 2025-05-20 14:35:47.123456


================================================================
SECCIÓN 8: FUNCIÓN buscar_cancion()
================================================================

  TIPO DE FUNCIÓN : VOID (no retorna ningún valor)
  PARÁMETROS      : Ninguno
  RETORNA         : Nada
  USA try/except  : Sí, para capturar errores de tipo ValueError
  COMPLEJIDAD     : O(n) — recorre la lista hasta encontrar

--------------------------------------------------------------
Código completo de la función:
--------------------------------------------------------------

    def buscar_cancion():
        try:
            codigo_buscar = int(input("Ingrese código: "))
            encontrado = False

            for cancion in playlist:
                if cancion["codigo"] == codigo_buscar:
                    print("\nCanción encontrada")
                    print("Nombre:", cancion["nombre"])
                    print("Artista:", cancion["artista"])
                    print("Agregada por:", cancion["amigo"])
                    encontrado = True
                    break

            if encontrado == False:
                print("Canción no encontrada")

        except ValueError:
            print("Error: debe ingresar un número")

--------------------------------------------------------------
Explicación línea por línea:
--------------------------------------------------------------

  def buscar_cancion():
  → Se define la función. No recibe parámetros.

  try:
  → Inicia el bloque de intento protegido contra errores.

  codigo_buscar = int(input("Ingrese código: "))
  → Pide al usuario el código de la canción que desea buscar.
  → input() recibe texto, int() lo convierte a número entero.
  → Si el usuario escribe letras, int() falla y activa el except.

  encontrado = False
  → Se crea una VARIABLE BANDERA (o variable lógica) con valor
    False (falso).
  → Su trabajo es "recordar" si la canción fue encontrada o no.
  → Inicia en False porque aún no se ha buscado nada.
  → Solo cambia a True si se encuentra la canción.

  for cancion in playlist:
  → Ciclo FOR que recorre toda la lista playlist.
  → COMPLEJIDAD Big O = O(n): en el peor caso recorre
    toda la lista sin encontrar nada.

  if cancion["codigo"] == codigo_buscar:
  → En cada iteración compara el código de la canción actual
    con el código que el usuario ingresó.
  → Si son iguales, se encontró la canción.

  print("\nCanción encontrada")
  → Informa que la búsqueda fue exitosa.

  print("Nombre:", cancion["nombre"])
  print("Artista:", cancion["artista"])
  print("Agregada por:", cancion["amigo"])
  → Muestra los datos de la canción encontrada.

  encontrado = True
  → Cambia la variable bandera a True para registrar que
    sí se encontró la canción.

  break
  → Detiene el ciclo FOR inmediatamente.
  → Una vez encontrada la canción, no tiene sentido seguir
    revisando el resto de la lista.

  if encontrado == False:
  → Después del ciclo, verifica si la bandera sigue en False.
  → Si nunca cambió a True, significa que ninguna canción
    tenía ese código.

  print("Canción no encontrada")
  → Informa al usuario que el código no existe en la playlist.

  except ValueError:
  → Captura el error si el usuario escribió letras en vez
    de un número para el código.

  print("Error: debe ingresar un número")
  → Muestra un mensaje claro sin romper el programa.


================================================================
SECCIÓN 9: FUNCIÓN estadisticas(lista)
================================================================

  TIPO DE FUNCIÓN : VOID (no retorna ningún valor)
  PARÁMETROS      : Lista
  RETORNA         : Nada
  LLAMA A         : calcular_duracion(playlist)
  USA             : math.sqrt(), if/elif/else

--------------------------------------------------------------
Código completo de la función:
--------------------------------------------------------------

    def estadisticas():
        cantidad = len(playlist)
        total    = calcular_duracion(playlist)

        print("Cantidad de canciones:", cantidad)
        print("Duración total:", total)

        if cantidad > 0:
            promedio = total / cantidad
            print("Promedio:", promedio)
            raiz = math.sqrt(promedio)
            print("Raíz del promedio:", raiz)

            if promedio >= 300:
                print("Playlist con canciones de duración larga")
            elif promedio >= 180:
                print("Playlist con canciones de duración media")
            else:
                print("Playlist con canciones de duración corta")
        else:
            print("No hay canciones registradas")

--------------------------------------------------------------
Explicación línea por línea:
--------------------------------------------------------------

  def estadisticas():
  → Se define la función. 
  → Recibe UN parámetro llamado "lista".
  → Este parámetro es la lista de canciones sobre la que
    se hará el cálculo. Se le pasará la variable
    global "playlist".

  cantidad = len(playlist)
  → len() cuenta cuántos elementos tiene la lista.
  → Ese número se guarda en "cantidad".

  total = calcular_duracion(playlist)
  → Llama a la función calcular_duracion() que ya estaba
    definida en el programa.
  → Le pasa la lista "playlist" como argumento.
  → Esa función recorre la lista, suma todas las duraciones
    y RETORNA el total.
  → El valor retornado se guarda en la variable "total".

  print("Cantidad de canciones:", cantidad)
  → Muestra en pantalla cuántas canciones hay en la playlist.

  print("Duración total:", total)
  → Muestra la duración total en segundos de toda la playlist.

  if cantidad > 0:
  → Verifica que haya al menos una canción antes de calcular
    el promedio.
  → Esto evita una división entre cero, que causaría un error.

  promedio = total / cantidad
  → Calcula el promedio de duración dividiendo el total
    entre la cantidad de canciones.
  → El operador "/" realiza división con decimales.

  print("Promedio:", promedio)
  → Muestra el promedio calculado en pantalla.

  raiz = math.sqrt(promedio)
  → Calcula la RAÍZ CUADRADA del promedio usando la
    librería math importada al inicio.
  → El resultado se guarda en la variable "raiz".

  print("Raíz del promedio:", raiz)
  → Muestra el resultado de la raíz cuadrada en pantalla.

  if promedio >= 300:
  → Primera condición: si el promedio es 300 segundos o más
    (5 minutos o más por canción).
  → Se considera duración LARGA.

  print("Playlist con canciones de duración larga")
  → Mensaje descriptivo si se cumple la condición anterior.

  elif promedio >= 180:
  → Segunda condición (solo se evalúa si la primera fue falsa):
    si el promedio está entre 180 y 299 segundos
    (entre 3 y 5 minutos por canción).
  → Se considera duración MEDIA.

  print("Playlist con canciones de duración media")
  → Mensaje descriptivo si se cumple esta segunda condición.

  else:
  → Si ninguna de las dos condiciones anteriores se cumplió,
    el promedio es menor a 180 segundos (menos de 3 minutos).
  → Se considera duración CORTA.

  print("Playlist con canciones de duración corta")
  → Mensaje descriptivo para canciones cortas.

  else: (del if cantidad > 0)
  → Si la playlist está vacía (cantidad == 0), se ejecuta
    este bloque en lugar de todos los cálculos.

  print("No hay canciones registradas")
  → Informa al usuario que no hay datos para calcular.

  Ejemplo completo de salida con 3 canciones (180, 240, 210 seg):

      Cantidad de canciones: 3
      Duración total: 630
      Promedio: 210.0
      Raíz del promedio: 14.491376746189438
      Playlist con canciones de duración media


================================================================
SECCIÓN 10: FUNCIÓN main() — FUNCIÓN PRINCIPAL
================================================================

  TIPO DE FUNCIÓN : VOID (controla el flujo del programa)
  PARÁMETROS      : Ninguno
  RETORNA         : Nada

--------------------------------------------------------------
¿Qué es la función main()?
--------------------------------------------------------------

  - Es el punto de entrada: desde aquí se llama a todas las
    demás funciones.
  - Contiene el CICLO PRINCIPAL que mantiene el programa
    funcionando hasta que el usuario decida salir.
  - Controla el flujo de decisiones según la opción elegida.

--------------------------------------------------------------
Estructura esperada de main():
--------------------------------------------------------------

  def main():                                          
    opcion = 0                                       

    # Ciclo while
    while opcion != 5:                               
        mostrar_menu()                               

        try:                                         

            opcion = int(input("Seleccione opción: ")) 

            # MATCH CASE
            match opcion:                            

                case 1:                              
                    agregar_cancion()                

                case 2:                              
                    mostrar_playlist()               

                case 3:                              
                    buscar_cancion()                

                case 4:                              
                    estadisticas()                   

                case 5:                              
                    print("Cerrando Spotify...")     

                case _:                              
                    print("Opción incorrecta")       

        except ValueError:                           

            print("Error: debe ingresar números")
                            
--------------------------------------------------------------
Explicación línea por línea:
--------------------------------------------------------------

  def main():
  → Se define la función principal del programa.
  → Es el punto de entrada: desde aquí se controla todo
    el flujo y se llaman todas las demás funciones.
  → No recibe parámetros.

  opcion = 0
  → Variable de control del ciclo principal.
  → Se inicia en 0 para que el ciclo arranque correctamente.
  → Cambiará según lo que el usuario elija en cada vuelta.

  while opcion != 5:
  → Ciclo WHILE (mientras) que mantiene el programa activo.
  → La condición dice: "continúa mientras la opción sea
    diferente de 5".
  → Cuando el usuario elige 5, la condición se vuelve falsa
    y el ciclo termina, cerrando el programa.
  → COMPLEJIDAD Big O = O(n): n es la cantidad de veces que
    el usuario interactúa con el menú antes de salir.

  mostrar_menu()
  → En cada vuelta del ciclo se llama la función mostrar_menu().
  → Esto muestra las 5 opciones al usuario antes de que elija.

  try:
  → Inicia el bloque de intento protegido.
  → Protege la lectura de la opción y la ejecución del match.

  opcion = int(input("Seleccione opción: "))
  → Lee la opción que el usuario escribe en el teclado.
  → input() recibe texto, int() lo convierte a número.
  → Si el usuario escribe letras, int() falla y activa
    el except ValueError.

  match opcion:
  → Estructura MATCH CASE (disponible desde Python 3.10).
  → Evalúa el valor de "opcion" y ejecuta el bloque que
    coincida con ese valor.
  → Es similar a un if/elif/else pero más limpio y legible
    cuando hay muchas opciones posibles.

  case 1:
      agregar_cancion()
  → Si el usuario eligió 1, se llama la función agregar_cancion().
  → Esa función pedirá los datos de la nueva canción.

  case 2:
      mostrar_playlist(playlist)
  → Si el usuario eligió 2, se llama mostrar_playlist()
    pasándole la lista global "playlist" como argumento.
  → Esa función mostrará todas las canciones guardadas.

  case 3:
      buscar_cancion()
  → Si el usuario eligió 3, se llama buscar_cancion().
  → Esa función pedirá un código y buscará la canción.

  case 4:
      estadisticas(playlist)
  → Si el usuario eligió 4, se llama estadisticas()
    pasándole la lista global "playlist" como argumento.
  → Esa función calculará y mostrará cantidad, total,
    promedio, raíz y clasificación de duración.

  case 5:
      print("Cerrando Spotify...")
  → Si el usuario eligió 5, imprime el mensaje de despedida.
  → En la siguiente verificación del while, opcion == 5,
    la condición "opcion != 5" será falsa y el ciclo termina.

  case _:
      print("Opción incorrecta")
  → El guion bajo _ es el caso por defecto.
  → Se ejecuta si el usuario ingresa cualquier número que
    no sea 1, 2, 3, 4 ni 5 (por ejemplo: 7, 99, -1).
  → Informa que la opción no es válida y el ciclo vuelve
    a mostrar el menú.

  except ValueError:
      print("Error: debe ingresar un número")
      opcion = 0
  → Se activa si el usuario escribió letras en la opción,
    como "hola" en lugar de un número.
  → opcion = 0 reinicia la variable para que el ciclo
    while continúe normalmente y no salga por error.

--------------------------------------------------------------
¿Por qué se escribe main() al final?
--------------------------------------------------------------

  main()

  → Esta línea al final del archivo es la que INICIA el programa.
  → En Python, definir una función no la ejecuta. Es necesario
    llamarla explícitamente.
  → Al escribir main() sola al final, se le dice a Python:
    "empieza aquí".


================================================================
RESUMEN DE CONCEPTOS CLAVE USADOS EN EL PROGRAMA
================================================================

  Concepto               Explicación breve
  -----------------------------------------------------------
  import                 Importa una librería externa.
  Lista []               Colección de elementos ordenados.
  Diccionario {}         Pares clave:valor para guardar datos.
  Variable global        Accesible por todas las funciones.
  Variable acumuladora   Inicia en 0 y va sumando valores.
  Función VOID           No retorna ningún valor útil.
  Función con RETURN     Calcula y devuelve un resultado.
  Ciclo FOR              Recorre cada elemento de una lista.
  Ciclo WHILE            Repite mientras una condición sea verdadera.
  Parámetro              Valor que recibe una función al llamarse.
  Big O                  Mide la eficiencia de un algoritmo.
  print()                Muestra mensajes en pantalla.
  input()                Lee un valor ingresado por el usuario.


================================================================
FIN 
================================================================
