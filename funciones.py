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