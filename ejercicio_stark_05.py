from data_stark import lista_personajes
from funciones import *
"""
    3. Desarrollar los siguientes puntos (usando el data_stark.py) -> Se deben
desarrollar funciones extra dependiendo de la situación o reutilizar funciones
anteriores como normalizar o listar.
● 1-Normalizar datos (No debe dejar de entrar a las otras opciones)
● 2-Generar CSV (Guardar la lista generada en otra variable)
● 3-Listar heroes del archivo CSV ordenados por altura ASC (Validar si el
mismo existe)
● 4-Generar JSON (Guardar la lista generada en otra variable)
● 5-Listar heroes del archivo JSON ordenados por peso DESC (Validar si
el mismo existe)
● 6-Ordenar Lista por fuerza (Se le tiene que preguntar al usuario si
ordenar de manera ASC o DESC
● 7-Salir
"""
try:
    menu = int(input('1-Normalizar datos (No debe dejar de entrar a las otras opciones) \n2-Generar CSV (Guardar la lista generada en otra variable)\n3-Listar heroes del archivo CSV ordenados por altura ASC (Validar si el mismo existe)\n4-Generar JSON (Guardar la lista generada en otra variable)\n5-Listar heroes del archivo JSON ordenados por peso DESC (Validar si el mismo existe)\n6-Ordenar Lista por fuerza (Se le tiene que preguntar al usuario si ordenar de manera ASC o DESC\n7 - Salir\n'))
except ValueError:
    print("Entrada inválida. Debe ingresar un número.")
    menu = int(input('Ingrese nuevamente: '))
while True:
    try:
        while menu != 1:
            menu = int(input('Debe ingresar 1:\n'))
        if menu == 1:
            lista_personajes_01 = convertir_datos(lista_personajes)
            opcion = int(input('1-Normalizar datos (No debe dejar de entrar a las otras opciones) \n2-Generar CSV (Guardar la lista generada en otra variable)\n3-Listar heroes del archivo CSV ordenados por altura ASC (Validar si el mismo existe)\n4-Generar JSON (Guardar la lista generada en otra variable)\n5-Listar heroes del archivo JSON ordenados por peso DESC (Validar si el mismo existe)\n6-Ordenar Lista por fuerza (Se le tiene que preguntar al usuario si ordenar de manera ASC o DESC\n7 - Salir\n'))
            match opcion:
                case 2:
                    lista_csv = generar_csv("personajes.csv",lista_personajes_01)
                case 3:
                    lista_altura_ascendente= ordenar_heroes_ascendentes(lista_personajes_01, "altura")
                    lista_csv_altura_ascendente = generar_csv("personajes_por_altura.csv",lista_altura_ascendente)
                    lista_csv_altura_ascendente_para_leer = "personajes_por_altura.csv"
                    superheroes_leidos=leer_csv(lista_csv_altura_ascendente_para_leer)
                case 4:
                    lista_json=generar_json("personajes.json",lista_personajes_01,"Heroes")
                case 5:
                    lista_peso_descendente= ordenar_descendente(lista_personajes_01, "peso")
                    lista_json_peso_descendente = generar_json("personajes_por_peso.json",lista_peso_descendente,"Heroes_peso_descendentes")
                    superheroes_leidos = leer_json("personajes_por_peso.json", "Heroes_peso_descendentes")
                case 6:
                    lista_de_fuerza=ordenar_heroes_por_clave(lista_personajes_01, "fuerza")
                    lista_json_fuerza = generar_json("personajes_fuerza.json",lista_de_fuerza,"Heroes_fuerza")
                    lista_csv_fuerza = generar_csv("personajes_fuerza.csv",lista_de_fuerza)
                case 7:
                    break
                case _:
                    print("comando invalido")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")
        menu = int(input('Ingrese nuevamente: '))