from data_stark import lista_personajes
from funciones import *

while True:
    opcion = input('')
    match opcion:
        case 'a':
            datos = stark_normalizar_datos(lista_personajes)
            respuesta(datos)
        case 'b':
            b = obtener_dato(lista_personajes, "fuerza")
            print(b)
        case 'c':
            c = obtener_nombre(lista_personajes)
            print(c)
        case 'd':
            obtener_nombre_y_dato(lista_personajes,'identidad')
        case 'e':
            e = obtener_maximo(lista_personajes, "peso")
            print(e)
        case 'f':
            f = obtener_minimo(lista_personajes, "peso")
            print(f)
        case 'g':
            g = obtener_dato_cantidad(lista_personajes, 183, "altura")
            print(g)
        case 'h':
            lista_mas_fuertes = obtener_dato_cantidad(lista_personajes,"maximo" ,"fuerza")
            stark_imprimir_heroes(lista_mas_fuertes)
        case 'i':
            i = sumar_dato_heroe(lista_personajes, "altura")
        case 'j':
            suma_de_fuerzas = sumar_dato_heroe(lista_personajes, "fuerza")
            lista_mas_fuertes = obtener_dato_cantidad(lista_personajes,"maximo" ,"fuerza")
            j = dividir(suma_de_fuerzas, len(lista_mas_fuertes))
            print(j)