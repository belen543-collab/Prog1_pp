import funciones

legajos = [23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49] 
alumnos = ["Lopez Laura", "Gomez Sofia", "Perez Juan", "Sanchez Daniel", "Rodriguez Maria", "Fernandez Pablo", "Diaz Ana", "Luna Carlos", "Torres Lucía", "Vega Jorge", "Silva Natalia", "Romero Miguel", "Ortiz Elena", "Castro David", "Ramos Beatriz", "Soto Santiago", "Navarro Camila", "Herrera Sebastián", "Mendoza Valentina", "Delgado Andrés", "Cruz Paula", "Guerrero José", "Reyes María José", "Molina Francisco", "Sánchez Carmen", "Ruíz Antonio", "Flores Lucía", "García Mateo", "Pérez Valeria"]
generos = ["f", "f", "m", "m" , "f", "m", "f", "m", "f", "m", "f", "m", "f", "m", "f", "m", "f", "m", "f", "m", "f", "m", "f", "m", "f", "m"]
notas_primer_parcial = [6,9,6,7,8,5,9,6,7,8,5,9,6,7,8,5,9,6,7,8,5,9,6,7,8,5]
notas_segundo_parcial = [7,4,8,8,5,9,4,8,5,9,4,8,5,9,4,8,5,9,3,8,9,6,4,5,6,7]

print("Bienvenido al sistema de gestión de datos de alumnos.")
while True:
    opcion = funciones.mostrar_menu()

    match opcion:
        case 1:
            while True:
                print(f"--- Cargar datos del alumno {len(alumnos)+1}--- ")

                nuevo_legajo = funciones.cargar_legajo()
                funciones.agregar_elemento(legajos,nuevo_legajo)

                nuevo_nombre = funciones.cargar_nombre()
                funciones.agregar_elemento(alumnos,nuevo_nombre)

                nuevo_genero = funciones.cargar_genero()
                funciones.agregar_elemento(generos,nuevo_genero)

                nueva_nota_pp = funciones.cargar_notas_primer_parcial()
                funciones.agregar_elemento(notas_primer_parcial,nueva_nota_pp)

                nueva_nota_sp = funciones.cargar_notas_segundo_parcial()
                funciones.agregar_elemento(notas_segundo_parcial,nueva_nota_sp)

                while True:
                    pregunta = input("¿Desea cargar datos de otro alumno? (s/n): ")
                    if pregunta == "s" or pregunta == "S" or pregunta == "n" or pregunta == "N":
                        break
                    print("Por favor, ingrese una opción válida. (s/n)")
                if pregunta == "n" or pregunta == "N":
                    break
        case 2:
            funciones.mostrar_informe(legajos, alumnos, generos, notas_primer_parcial, notas_segundo_parcial)

        case 3:
            promedio = funciones.calcular_promedios(notas_primer_parcial, notas_segundo_parcial)

        case 7:
            print("Cerrando el programa.")
            exit()
            
    if not funciones.preguntar_volver_menu():
        break
