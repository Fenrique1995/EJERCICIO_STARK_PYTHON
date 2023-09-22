"""
6.Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes y se encargará de la ejecución principal de nuestro programa. 
Utilizar if/elif o match según prefiera. Debe informar por consola en caso de seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.
"""

from data_stark import lista_personajes
from funciones import *
"""
7. Una vez realizadas y probadas las funciones resolver en un menú los siguientes puntos del desafio anterior.
"""
while True:
    #opcion = input('')
    opcion = stark_menu_principal()
    match opcion:
        #A.Normalizar datos (No se debe poder acceder a los otros puntos)
        case '1':
            datos = stark_normalizar_datos(lista_personajes)
            respuesta(datos)
        #B.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
        case '4':
            heroes_nb(lista_personajes)
        #C.Recorrer la lista y determinar cuál es el superhéroe más alto de género F
        case '2':
            heroina_mas_alta(lista_personajes)
        #D.Recorrer la lista y determinar cuál es el superhéroe más alto de género M
        case '3':
            heroe_mas_alto(lista_personajes)
        #E.Recorrer la lista y determinar cuál es el superhéroe más débil de género M 
        case '5':
            heroe_masculino_mas_debil(lista_personajes)
        #F.Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
        case '6':
            heroe_nb_mas_debil(lista_personajes)
        #G.Recorrer la lista y determinar la fuerza promedio de los  superhéroes de género NB
        case '7':
            fuerza_heroes_nb_promedio(lista_personajes)
        #H.Determinar cuántos superhéroes tienen cada tipo de color de ojos.
        case '8':
            color_de_ojos(lista_personajes)
        #I.Determinar cuántos superhéroes tienen cada tipo de color de pelo.
        case '9':
            color_de_pelo(lista_personajes)
        #J:Listar todos los superhéroes agrupados por color de ojos.
        case '10':
            lista_por_color_de_ojos(lista_personajes)
        #K.Listar todos los superhéroes agrupados por tipo de inteligencia
        case '11':
            lista_por_tipo_de_inteligencia(lista_personajes)
        case _:
            print('debe ingresar uno de los numeros pertinentes: \n')