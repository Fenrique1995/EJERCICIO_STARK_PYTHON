from data_stark import lista_personajes
from funciones import *
"""
6. Crear funciones para el manejo del menú principal (usar de guía el anterior desafio)
El menú principal debe tener las siguientes opciones
    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Imprimir la lista de nombres y el código del mismo
    3 - Normalizar datos
    4 - Imprimir índice de nombres 
    5 - Navegar fichas 
    6 - Salir
"""
while True: 
    menu = input('ingrese numero: \n1 - Imprimir la lista de nombres junto con sus iniciales\n2 - Imprimir la lista de nombres y el código del mismo\n3 - Normalizar datos\n4 - Imprimir índice de nombres \n5 - Navegar fichas \n6 - Salir\n')
    match menu:
        case "1":
            names = obtener_nombre(lista_personajes)
            stark_imprimir_nombres_con_iniciales(names)
        case "2":
            stark_generar_codigos_heroes(lista_personajes)
        case "3":
            stark_normalizar_datos(lista_personajes)
        case "4":
            stark_imprimir_indice_nombre(lista_personajes)
        case "5":
            stark_navegar_fichas(lista_personajes)
        case "6":
            break
