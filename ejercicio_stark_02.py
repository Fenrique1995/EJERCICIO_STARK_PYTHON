from data_stark import lista_personajes
from funciones import *

while True:
    letra = input('ingrese 1)')
    opcion = letra.upper()
    match opcion:
        case "A":
            heroes_nb(lista_personajes)
        case "B":
            heroina_mas_alta(lista_personajes)
        case "C":
            heroe_mas_alto(lista_personajes)
        case "D":
            heroe_masculino_mas_debil(lista_personajes)
        case "E":
            heroe_nb_mas_debil(lista_personajes)
        case "F":
            fuerza_heroes_nb_promedio(lista_personajes)
        case "G":
            color_de_ojos(lista_personajes)
        case "H":
            color_de_pelo(lista_personajes)
        case "I":
            lista_por_color_de_ojos(lista_personajes)
        case "J":
            lista_por_tipo_de_inteligencia(lista_personajes)
        case "Z":
            break