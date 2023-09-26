from data_stark import lista_personajes
from funciones import *

while True:
    seguro = ["A","B","C","D","E","F","G","H","I","J","Z"]
    letra = input('ingrese \nA.heroes no binarios\nB.heroina mas alta\nC.heroe mas alto\nD.heroe masculino mas debil\nE.heroe no binario mas debil\nF.el promedio de la fuerza de los heroes no binarios\nG.cantidad y tipo de ojos\nH.cantidad y tipo de cabellos\nI.listado por color de ojos\nJ.lista por tipo de inteligencia\nZ)salir\n')
    opcion = letra.upper()
    while opcion != seguro[0] and opcion != seguro[1] and opcion != seguro[2] and opcion != seguro[3] and opcion != seguro[4] and opcion != seguro[5] and opcion != seguro[6] and opcion != seguro[7] and opcion != seguro[8] and opcion != seguro[9] and opcion != seguro[10]:
        letra = input('Debe ingresar (A,B,C,D,E,F,G,H,I,J,Z)\n')
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