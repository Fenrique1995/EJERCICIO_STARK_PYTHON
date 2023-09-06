from data_stark import lista_personajes
from funciones import *



while True:
    num = int(input("Ingrese que desea hacer:\n1)Recorrer toda la lista: \n2)heroe mas fuerte\n3)heroe mas debil\n4)peso promedio de los heroes masculinos\n5)lista de heroes que superan en fuerza al promedio de heroinas\n9)salir\n"))
    
    match num:
        case 1:
            recorrer_todo(lista_personajes)
        case 2:
            heroe_mas_fuerte(lista_personajes)
        case 3:
            heroe_mas_debil(lista_personajes)
        case 4:
            peso_promedio_masculinos(lista_personajes)
        case 5:
            lista_y_peso_heroes_fuerza_mayor(lista_personajes)
        case 9:
            break