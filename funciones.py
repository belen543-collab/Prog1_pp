def cargar_legajo()->int:
    #al ser ingresado un numero de legajo, lo valida.
    #devuelve un numero entero.
    while True:
        legajo = input("Ingrese el número de legajo del alumno: ")
        bandera = True
        for i in legajo:
            caracter = ord(i)
            if not (48 <= caracter <= 57):
                bandera = False
                break
        if bandera:
            legajo = int(legajo)
            return legajo
        print("El legajo debe contener solo números. Por favor, ingrese un legajo válido.")

   

def agregar_elemento(lista, elemento):
    #Añade un elemento a la lista.
    lista[len(lista):] = [elemento]


def cargar_nombre() -> str:
    #permite ingresar un nombre y valida que solo contenga datos alfabéticos.
    #devuelve el nombre del alumno.
    letras_especiales = [32, 193, 201, 205, 211, 218, 220, 209, 225, 233, 237, 243, 250, 252, 241]
    while True:
         nombre = input("Ingrese el nombre del alumno: ")
         bandera = True
         for letra in nombre:
                codigo = ord(letra)
                es_valida = (65 <= codigo <= 90) or (97 <= codigo <= 122) or (codigo in letras_especiales)
                if not es_valida:
                    bandera = False
                    break
         if bandera:
             return nombre
         else:
             print("El nombre debe contener solo letras. Por favor, ingrese un nombre válido.")

def cargar_genero() -> str:
    #permite ingresar el género del alumno y valida que sea F, M o X.
    #devuelve el género del alumno.
    valores_aceptados = ["F", "f", "M", "m", "X", "x"]
    while True:
        genero = input("Ingrese el género del alumno: (F/M/X) ")
        bandera = True

        for i in valores_aceptados:
            if genero == i:
                 return genero
            
        print("Por favor, ingrese un género válido. (F/M/X)")


def cargar_notas_primer_parcial() -> int:
    #permite ingresar notas del primer parcial del 1 hasta el 10.

    valores_aceptados = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    while True:
        nota = (input("Ingrese la nota del primer parcial: "))
        for i in valores_aceptados:
            if nota == i:
                 nota = int(nota)
                 return nota
        print("Por favor, la nota debe ser entre 0 y 10.")

def cargar_notas_segundo_parcial() -> int:
    #permite ingresar notas del segundo parcial del 1 hasta el 10.
    #devuelve la nota del segundo parcial.
    valores_aceptados = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    while True:
        nota = (input("Ingrese la nota del segundo parcial: "))
        for i in valores_aceptados:
            if nota == i:
                 nota = int(nota)
                 return nota
        print("Por favor, la nota debe ser entre 0 y 10.")

def mostrar_informe(legajos, alumnos, generos, notas_primer_parcial, notas_segundo_parcial):
    #Muestra un informe con los datos de los alumnos.
    print("--- INFORME DE DATOS ---")
    print("Legajo\tAlumnos\t\t\tGenero\tPrimer Parcial\tSegundo Parcial")
    for i in range(len(legajos)):
        print(f"{legajos[i]}\t{alumnos[i]}\t\t{generos[i]}\t\t{notas_primer_parcial[i]}\t\t{notas_segundo_parcial[i]}")

def mostrar_menu()->int:
    # Muestra las opciones del menú 
    # Devuelve un número.
    while True:
        print("Seleccione una opción:")
        print("1. Cargar datos de alumnos")
        print("2. Ver informe con los datos")
        print("3. Calcular promedio de notas")
        print("4. Ver promedios ordenados")
        print("5. Ver mejores promedios")
        print("6. Ver datos individuales de los alumnos")
        print("7. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")
        bandera = True
        for i in opcion:
            caracter = ord(i)
            if not (49 <= caracter <= 55):
                bandera = False
                break
        if bandera:
            opcion = int(opcion)
            return opcion
        print("Por favor, ingrese un número entre 1 y 7.")

def preguntar_volver_menu()->bool:
    # Pregunta al usuario si desea volver al menú.
    # Devuelve True o False.
    while True:
        respuesta = input("¿Desea volver al menú? (s/n): ")
        if respuesta == "s" or respuesta == "S": 
            return True
        if respuesta == "n" or respuesta == "N":
            return False
        else:
            print("Por favor, ingrese 's' o 'n'.")

def calcular_promedios(notas_primer_parcial, notas_segundo_parcial):
    # Calcula el promedio de las notas de los alumnos.
    # Devuelve una lista con los promedios.
    print("--- PROMEDIOS DE NOTAS ---")
    for i in range(len(notas_primer_parcial)):
        promedio = (notas_primer_parcial[i] + notas_segundo_parcial[i]) / 2
        print(f"\t{promedio}")
