import math, copy
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
        heroe["color_ojos"] = heroe["color_ojos"].upper()
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
        if heroe['color_pelo'] != "":
            heroe['color_pelo'] = heroe['color_pelo'].upper()
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
        color_ojos = heroe["color_ojos"].upper()
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

#######Ejercicio Stark 3########
"""
    0. Crear la función 'stark_normalizar_datos()' la cual recibirá por parámetro la lista de héroes. La función deberá:
    • Recorrer la lista y convertir al tipo de dato correcto las keys (solo con las keys que representan datos numéricos) por ejemplo fuerza (int), altura (float), etc
    • Validar primero que el tipo de dato no sea del tipo al cual será casteado. Por ejemplo si una key debería ser entero (ejemplo fuerza) verificar antes que no se encuentre ya en ese tipo de dato.
    • Si al menos un dato fue modificado, la función deberá retornar el valor booleano True
    • En caso de que la lista esté vacía o ya se hayan normalizado anteriormente los datos se deberá retornar el valor booleano False
    • Crear una opción en el menú que me permita normalizar los datos (No se debería poder acceder a ninguna otra opción del menú hasta que los datos esten normalizados)
    • En caso de que la llamada a la función retorne True mostrar un mensaje diciendo “Datos Normalizados” sino mostrar el mensaje “Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente”
"""
def stark_normalizar_datos(lista):
    lista_copiada = copy.deepcopy(lista)
    for heroe in lista_copiada:
        if not isinstance(heroe["altura"] and heroe["peso"] and heroe["fuerza"], (float, int)):
            heroe["altura"] = float(heroe["altura"] )
            heroe["peso"] = float(heroe["peso"])
            heroe["fuerza"] = int(heroe["fuerza"])
            return True
        else:
            return False
def respuesta(dato):
    if dato == True:
        print("Datos Normalizados")
    else:
        print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")

"""
1.1Crear la función ”obtener_dato()” la cual recibirá por parámetro un diccionario el cual representara a un héroe y también recibirá un string que hace referencia a una “clave” del mismo
Validar siempre que el diccionario no esté vacío y que el mismo tenga una key llamada “nombre”. Caso contrario la función retornara un False
"""
def obtener_dato(lista, clave):
    lista_copiada = copy.deepcopy(lista)
    dato = []
    for heroe in lista_copiada:
        if clave in heroe:
            dato.append({clave:heroe[clave]})
        else:
            return False
    return dato

"""
1.2Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el cual representara a un héroe y devolverá un string el cual contenga su nombre formateado de la siguiente manera: 
Nombre: Howard the Duck
Validar siempre que el diccionario no este vacío y que la key que se pide exista. Caso contrario la función retornara un False
NOTA: Reutilizar la función creada en el punto anterior
"""

def obtener_nombre(lista):
    lista_copiada = copy.deepcopy(lista)
    lista_resultante = []
    for persona in lista_copiada:
        nombre = persona.get("nombre")
        if nombre is not None:
            nuevo_diccionario = {"nombre": nombre}
            lista_resultante.append(nuevo_diccionario)
    return lista_resultante


"""
    2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario el cual representara a un héroe y una key (string) la cual representará el dato que se desea obtener. 

    • La función deberá devolver un string el cual contenga el nombre y dato (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.

    • El string resultante debe estar formateado de la siguiente manera: (suponiendo que la key es fuerza)
Nombre: Venom | fuerza: 500
    • Validar siempre que la lista no este vacía. Caso contrario la función retornara un False
NOTA: Reutilizar las funciones del punto anterior
"""

def obtener_nombre_y_dato(lista, atributo):
    lista_copiada = copy.deepcopy(lista)
    nombres = obtener_nombre(lista_copiada)
    for nombre in nombres:
        nombre.get('nombre')

    
    dato = obtener_dato(lista_copiada, atributo)
    for nombre, clave in zip(nombres, dato):
            mensaje_01 ="Nombre: "+nombre.get('nombre')
            mensaje_02 =" | "+ atributo+": "+clave[atributo]
            print(mensaje_01+mensaje_02)


"""
3.1 Crear la función “obtener_maximo()” la cual recibirá como parámetro una lista y una key (string) la cual representará el dato al cual se le debe calcular su cantidad MÁXIMA.
    • Validar siempre que la lista no esté vacía y que el dato que está buscando sea un int o un float. Caso contrario la función retornara un False
    • En caso de que el dato que se está buscando en el diccionario es de tipo int o float retornar el mayor que haya encontrado en la búsqueda.
"""
def obtener_maximo(lista, atributo):
    lista_copiada = copy.deepcopy(lista)
    numero_maximo=-1
    for heroe in lista_copiada:
        if not isinstance(heroe[atributo], (float, int)):
            heroe["altura"] = math.floor(float(heroe.get(atributo)))
            heroe["peso"] = round(float(heroe.get(atributo)))
            heroe["fuerza"] = int(heroe.get(atributo))
            if heroe[atributo]> numero_maximo:
                numero_maximo = heroe[atributo]
        else:
            return False
    return numero_maximo

"""
3.2 Crear la función “obtener_minimo()” la cual recibirá como parámetro una lista y una key (string) la cual representará el dato al cual se le debe calcular su cantidad MÍNIMA.
    • Validar siempre que la lista no esté vacía y que el dato que está buscando sea un int o un float. Caso contrario la función retornara un False
    • En caso de que el dato que se está buscando en el diccionario es de tipo int o float retornar el menor que haya encontrado en la búsqueda.
"""

def obtener_minimo(lista, atributo):
    lista_copiada = copy.deepcopy(lista)
    numero_minimo= 100
    for heroe in lista_copiada:
        if not isinstance(heroe[atributo], (float, int)):
            heroe["altura"] = math.floor(float(heroe["altura"]))
            heroe["peso"] = round(float(heroe["peso"]))
            heroe["fuerza"] = int(heroe["fuerza"])
            if numero_minimo > heroe[atributo]:
                numero_minimo = heroe[atributo]
        else:
            return False
    return numero_minimo

"""
3.3 Crear la función 'obtener_dato_cantidad()' la cual recibira tres parámetros:

    • La lista de héroes
    • Un número que me indique el valor a buscar (puede ser la altura máxima, la altura mínima o cualquier otro dato)
    • Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
La función deberá retornar una lista con el héroe o los heroes que cumplan  con la condición pedida. Reutilizar las funciones hechas en los puntos 3.1 y 3.2
Ejemplo de llamada:
mayor_altura = obtener_maximo(lista_heroes,”altura”)
lista_heroes_max_altura = 'obtener_dato_cantidad(lista_heroes,mayor_altura,”altura”)
El objetivo de estás llamadas es obtener todos los superhéroes que tengan la altura correspondiente a la altura máxima, y la misma función me podria servir tanto como para altura menor, como la mayor o alguna altura que yo le especifique también.
"""

def obtener_dato_cantidad(lista, maxima_o_minima, atributo):
    lista_copiada = copy.deepcopy(lista)
    lista_segun_el_dato = []
    el_maximo = maxima_o_minima
    el_minimo = maxima_o_minima
    if maxima_o_minima == "maximo":
        el_maximo = obtener_maximo(lista_copiada, atributo)
    elif maxima_o_minima == "minimo":
        el_minimo = obtener_minimo(lista_copiada, atributo)
    for heroe in lista_copiada:
        if not isinstance(heroe[atributo], (float, int)):
            heroe["altura"] = math.floor(float(heroe["altura"]))
            heroe["peso"] = round(float(heroe["peso"]))
            heroe["fuerza"] = int(heroe["fuerza"])
        if heroe[atributo] == el_maximo:
            lista_segun_el_dato.append(heroe)
        elif heroe[atributo] == el_minimo:
            lista_segun_el_dato.append(heroe)
    return lista_segun_el_dato

"""
3.4 Crear la función 'stark_imprimir_heroes'  la cual recibirá un parametro: 

    • La lista de héroes

Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara False
En caso de que la lista no este vacia imprimir la información completa de todos los heroes de la lista que se le pase
Ejemplo de llamada:
mas_pesado = obtener_maximo(lista_heroes,”peso”)
lista_mas_pesados = 'obtener_dato_cantidad(lista_heroes,mas_pesado ,”peso”)
stark_imprimir_heroes(lista_mas_pesados) -> Imprimo sólo los héroes más pesados
stark_imprimir_heroes(lista_heroes) -> Imprimo todos los héroes
"""

def stark_imprimir_heroes(lista):
    if len(lista) > 0:
        for heroe in lista:
            print(heroe)

"""
4.1 Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de héroes y un string que representara el dato/key de los héroes que se requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes de hacer la suma. La función deberá retorna la suma de todos los datos según la key pasada por parámetro
"""
def sumar_dato_heroe(lista, clave):
    lista_copiada = copy.deepcopy(lista)
    suma_de_datos = 0
    for heroe in lista_copiada:
        if not isinstance(heroe[clave], (float, int)):
            heroe["altura"] = math.floor(float(heroe[clave]))
            heroe["peso"] = round(float(heroe[clave]))
            heroe["fuerza"] = int(heroe[clave])
        if isinstance(heroe, dict) and heroe: 
            if clave in heroe:
                suma_de_datos += heroe[clave]
    return suma_de_datos

"""
4.2 Crear la función  ‘dividir’ la cual recibirá como parámetro dos números (dividendo y divisor). Se debe verificar si el divisor es 0,  en caso de serlo, retornar False, caso contrario realizar la división entre los parámetros y retornar el resultado
"""
def dividir(dividendo, divisor):
    if divisor > 0:
        resultado = round(dividendo / divisor)
        return resultado
    else:
        return False

"""
4.3 Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de héroes y un string que representa el dato del héroe que se requiere calcular el promedio. La función debe retornar el promedio del dato pasado por parámetro
"""

def calcular_promedio(lista, atributo):
    lista_copiada = copy.deepcopy(lista)
    suma_de_todo = sumar_dato_heroe(lista_copiada, atributo)
    contador = 0
    promedio = 0
    for heroe in lista_copiada:
        contador += 1
        if not isinstance(heroe[atributo], (float, int)):
            heroe["altura"] = math.floor(float(heroe[atributo]))
            heroe["peso"] = round(float(heroe[atributo]))
            heroe["fuerza"] = int(heroe[atributo])
    promedio = round(suma_de_todo/contador)
    return promedio

"""
4.4 Crear la función ‘mostrar_promedio_dato’ la cual recibirá como parámetro una lista de héroes y un string que representa la clave del dato
    • Se debe validar que el dato que se encuentra en esa clave sea de tipo int o float. Caso contrario retornaria False
    • Se debe validar que la lista a manipular no esté vacía , en caso de que esté vacía se retornaria también False
"""

def mostrar_promedio_dato(lista, dato):
    lista_copiada = copy.deepcopy(lista)
    el_promedio = calcular_promedio(lista_copiada, dato)
    for heroe in lista_copiada:
        if not isinstance(heroe[dato], (float, int)):
            heroe["altura"] = math.floor(float(heroe[dato]))
            heroe["peso"] = round(float(heroe[dato]))
            heroe["fuerza"] = int(heroe[dato])
        else:
            return False
    mensaje = "El promedio de "+dato+" es: "+str(el_promedio)
    print(mensaje)

"""
5.1 Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla, el cual permite utilizar toda la funcionalidad ya programada.
"""

def imprimir_menu():
    menu = input('el menu: \n ingrese:\n1-Normalizar datos\n2-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\n3-Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n4-Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n5-Recorrer la lista y determinar cuál es el superhéroe más débil de género M \n6-Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n7-Recorrer la lista y determinar la fuerza promedio de los  superhéroes de género NB\n8-Determinar cuántos superhéroes tienen cada tipo de color de ojos\n9-Determinar cuántos superhéroes tienen cada tipo de color de pelo\n10-Listar todos los superhéroes agrupados por color de ojos\n11-Listar todos los superhéroes agrupados por tipo de inteligencia\n')
    return menu

"""
5.2 Crear la función “validar_entero” la cual recibirá por parámetro un string de número el cual deberá verificar que sea sea un string conformado únicamente por dígitos. Retornara True en caso de serlo, False caso contrario
"""

def validar_entero(numero):
    if numero.isdigit():
        return True
    else:
        return False

"""
5.3 Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú de opciones y le pedirá al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara casteado a int , caso contrario retorna False. Reutilizar las funciones del ejercicio 5.1 y 5.2
"""

def stark_menu_principal():
    digito = imprimir_menu()
    validar_entero(digito)
    return digito