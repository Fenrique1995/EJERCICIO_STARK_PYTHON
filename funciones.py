# A.Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
def recorrer_todo(lista):
    for i in lista:
        print(i)

#B.Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)

def heroe_mas_fuerte(lista):
    fuerza_maxima = -1
    super_heroe_mas_fuerte = None
    for heroe in lista:
        heroe["fuerza"] = int(heroe["fuerza"])
        if heroe["fuerza"] > fuerza_maxima:
            fuerza_maxima = heroe["fuerza"]
            super_heroe_mas_fuerte = heroe
    
    print(super_heroe_mas_fuerte["identidad"], super_heroe_mas_fuerte["peso"])

#C.Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)

def heroe_mas_debil(lista):
    fuerza_maxima = 1000
    superheroe_mas_debil = None
    for heroe in lista:
        heroe["fuerza"] = int(heroe["fuerza"])
        if heroe["fuerza"] < fuerza_maxima:
            fuerza_maxima = heroe["fuerza"]
            superheroe_mas_debil = heroe
    
    print(superheroe_mas_debil["nombre"], superheroe_mas_debil["identidad"])


#D.Recorrer la lista y determinar el peso promedio de los  superhéroes masculinos (PROMEDIO)

def peso_promedio_masculinos(lista):
    peso_total = 0
    peso_promedio = 0
    counter = 0
    for heroe in lista:
        if heroe["genero"] == "M":
            counter += 1
            peso_total += float(heroe["peso"])

    peso_promedio = round(peso_total / counter)
    print('Peso promedio: '+str(peso_promedio)+' kilos')

#E.Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino

def fuerza_promedio_femeninas(lista):
    fuerza_total = 0
    fuerza_promedio = 0
    counter = 0
    for heroe in lista:
        if heroe["genero"] == "F":
            counter += 1
            fuerza_total += int(heroe["fuerza"])
    
    fuerza_promedio = fuerza_total / counter
    return fuerza_promedio

def lista_y_peso_heroes_fuerza_mayor(lista):
    for heroe in lista:
        fuerza_promedio = fuerza_promedio_femeninas(lista)
        fuerza = int(heroe["fuerza"])
        peso = round(float(heroe["peso"]))
        if fuerza > fuerza_promedio:
            print(heroe["nombre"])
            print(peso)

#####Ejercicio Stark 2#######

#A.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
def heroes_nb(lista):
    for heroe in lista:
        if heroe["genero"] == "NB":
            print(heroe["nombre"])

#B.Recorrer la lista y determinar cuál es el superhéroe más alto de género F
def heroina_mas_alta(lista):
    altura_maxima = -1
    heroina_mas_alta = None
    for heroe in lista:
        if heroe["genero"] == "F":
            altura = float(heroe["altura"])
            if altura > altura_maxima:
                altura_maxima = altura
                heroina_mas_alta = heroe["nombre"]
    print(heroina_mas_alta)

#C.Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def heroe_mas_alto(lista):
    altura_maxima = -1
    heroe_mas_alto = None
    for heroe in lista:
        if heroe["genero"] == "M":
            altura = float(heroe["altura"])
            if altura > altura_maxima:
                altura_maxima = altura
                heroe_mas_alto = heroe["nombre"]
    print(heroe_mas_alto)

#D.Recorrer la lista y determinar cuál es el superhéroe más débil de género M 
def heroe_masculino_mas_debil(lista):
    fuerza_maxima=10000
    super_heroe_masculino_mas_debil= None
    for heroe in lista:
        if heroe["genero"] == "M":
            fuerza = int(heroe["fuerza"])
            if fuerza < fuerza_maxima:
                fuerza_maxima = fuerza
                super_heroe_masculino_mas_debil = heroe["nombre"]
    print(super_heroe_masculino_mas_debil)

#E.Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
def heroe_nb_mas_debil(lista):
    fuerza_maxima=10000
    super_heroe_nb_mas_debil= None
    for heroe in lista:
        if heroe["genero"] == "NB":
            fuerza = int(heroe["fuerza"])
            if fuerza < fuerza_maxima:
                fuerza_maxima = fuerza
                super_heroe_nb_mas_debil = heroe["nombre"]
    print(super_heroe_nb_mas_debil)

#F.Recorrer la lista y determinar la fuerza promedio de los  superhéroes de género NB
def fuerza_heroes_nb_promedio(lista):
    fuerza_total = 0
    fuerza_promedio = 0
    counter = 0
    for heroe in lista:
        if heroe["genero"] == "NB":
            counter += 1
            fuerza_total += int(heroe["fuerza"])
    
    fuerza_promedio = int(fuerza_total / counter)
    print(fuerza_promedio)

#G.Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def color_de_ojos(lista):
    conteo_colores_ojos = {}

    for heroe in lista:
        color_ojos = heroe["color_ojos"]
        if color_ojos in conteo_colores_ojos:
            conteo_colores_ojos[color_ojos] += 1
        else:
            conteo_colores_ojos[color_ojos] = 1

    for color_ojos, cantidad in conteo_colores_ojos.items():
        print(f"Hay {cantidad} superhéroes con ojos de color {color_ojos}.")

#H.Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def color_de_pelo(lista):
    conteo_colores_pelo = {}

    for heroe in lista:
        color_pelo = heroe["color_pelo"]
        if color_pelo in conteo_colores_pelo:
            conteo_colores_pelo[color_pelo] += 1
        else:
            conteo_colores_pelo[color_pelo] = 1

    for color_pelo, cantidad in conteo_colores_pelo.items():
        print(f"Hay {cantidad} superhéroes con cabello de color {color_pelo}.")

#I.Listar todos los superhéroes agrupados por color de ojos.
def lista_por_color_de_ojos(lista):
    superheroes_por_color = {}

    for heroe in lista:
        color_ojos = heroe["color_ojos"]
        nombre = heroe["nombre"]
        if color_ojos in superheroes_por_color:
            superheroes_por_color[color_ojos].append(nombre)
        else:
            superheroes_por_color[color_ojos] = [nombre]

    for color, lista_heroes in superheroes_por_color.items():
        print(f"Color de ojos: {color}")
        for heroe in lista_heroes:
            print(f"  - {heroe}")
        print()

#J.Listar todos los superhéroes agrupados por tipo de inteligencia
def lista_por_tipo_de_inteligencia(lista):
    superheroes_por_inteligencia = {}

    for heroe in lista:
        inteligencia_heroe = heroe["inteligencia"]
        nombre = heroe["nombre"]
        if inteligencia_heroe in superheroes_por_inteligencia:
            superheroes_por_inteligencia[inteligencia_heroe].append(nombre)
        else:
            superheroes_por_inteligencia[inteligencia_heroe] = [nombre]

    for inteligencia, lista_heroes in superheroes_por_inteligencia.items():
        print(f"tipo de inteligencia: {inteligencia}")
        for heroe in lista_heroes:
            print(f"  - {heroe}")
        print()