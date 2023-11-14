import math, copy, re, json, csv
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
        return round(dividendo / divisor)
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



##############Ejercicio Stark 4###############
"""
1.1. Crear la función ‘extraer_iniciales’ que recibirá como parámetro: 
    • nombre_heroe: un string con el nombre del personaje
La función deberá devolver a partir del parámetro recibido un nuevo string con las iniciales del nombre del personaje seguidos por un punto (.)
    • En el caso que el nombre del personaje contenga el artículo ‘the’ se deberá omitir de las iniciales
    • Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso que lo tenga se deberá reemplazar por un espacio en blanco
La función deberá validar:
    • Que el string recibido no se encuentre vacío
Devolver ‘N/A’ en caso de no cumplirse la validación

Ejemplo de la salida de la función para Howard the Duck:
H.D.
ATENCIÓN: Usar regex
"""
def extraer_iniciales(input_str):
    name_filtered = re.sub('-', ' ', input_str)
    match = re.findall(r'\b(?!the)\w', name_filtered, re.IGNORECASE)
    if match:
        initial = '.'.join(match)+"."
    else:
        return 'N/A'
    return initial
"""
1.2. Crear la función obtener_dato_formato’ la cual recibirá como parámetro:
    • dato: un string con un dato especifico
La función deberá convertir el dato pasado a minúsculas y con formato snake_case 
por ejemplo: Howard the Duck -> howard_the_duck
La función deberá validar:
    • Que el dato recibido sea del tipo str
En caso de encontrar algún error retornar False, caso contrario el nombre con el formato especificado
ATENCIÓN: Usar regex
"""
def obtener_dato_formato(input_str):
    if not isinstance(input_str, str):
        return False

    snake_case_str = re.sub(r'[^a-zA-Z0-9]+', '_', input_str)

    snake_case_str = snake_case_str.lower()

    snake_case_str = snake_case_str.strip('_')

    return snake_case_str
"""
1.3. Crear la función ‘stark_imprimir_nombre_con_iniciales’ la cual recibirá como parámetro:
    • nombre_heroe: un string con el nombre del personaje
	Se deberá validar:
    • Que el dato recibido sea del tipo diccionario
    • Que el  diccionario contengan la clave ‘nombre’  
La función deberá imprimir el dato en cuestión con el siguiente formato
Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de viñeta) seguido de un espacio.
Si el superhéroe es Howard the Duck se deberá mostrar 
* howard_the_duck (H.W.)
La función deberá devolver True en caso de haber finalizado con éxito o False en caso de que haya ocurrido un error
"""
def stark_imprimir_nombre_con_iniciales(input_str):
    if isinstance(input_str, dict) and 'nombre' in input_str:
        name = input_str['nombre']
        format_name_lower_case = obtener_dato_formato(name)
        initials = extraer_iniciales(name)

        return f"{format_name_lower_case} ({initials})"
    return False
"""
1.4 Crear la función ‘stark_imprimir_nombres_con_iniciales’  la cual recibirá como parámetro:
    • lista_heroes: la lista de personajes
La función deberá utilizar la función anterior 
Luego deberá imprimir la lista completa de los nombres de los personajes con el mismo formato de la anterior
	Se deberá validar:
    • Que lista_heroes sea del tipo lista
    • Que la lista contenga al menos un elemento
	La función retornara True si salió todo bien y False si ocurrió algún error
"""
def stark_imprimir_nombres_con_iniciales(lista):
    if not isinstance(lista, list) and not lista:
        return False
    for subject in lista:
        if not isinstance(subject, dict) and 'nombre' not in subject:
            return False
        print(stark_imprimir_nombre_con_iniciales(subject))
"""
2.1. Crear la función ‘generar_codigo_heroe’ la cual recibirá como parámetro:
    • diccionario de un héroe
    • id (int)
La función deberá generar un string con el siguiente formato:
    GENERO-X00…000ID
Es decir, el género recibido por parámetro seguido de un ‘-’ (guión) y por último el identificador recibido.  Todos los códigos generados deben tener como máximo 10 caracteres (contando todos los caracteres, inclusive el guión). Se deberá completar con ceros para que todos queden del mismo largo.
Dependiendo del género el primer número del código variará
En caso de que sea un superhéroe de género M -> el código comenzará en 1
En caso de que sea un superhéroe de género F-> el código comenzará en 2
En caso de que sea un superhéroe de género NB-> el código comenzará en 0
Algunos ejemplos:
    F-20000001 (10 caracteres)
	M-10000002 (10 caracteres)
	NB-0000010 (10 caracteres)
La función deberá validar:
    • El género no se encuentre vacío y este dentro de los valores esperados (‘M’,  ‘F’ o ‘NB’)
En caso de no pasar las validaciones retornar ‘N/A’. En caso de verificarse correctamente retornar el código generado.
"""
def generar_codigo_heroe(heroe, id):
    genero = heroe['genero'].upper()
    
    # Define un patrón de regex para validar el género y extraer el primer número
    patron = r'^(M|F|NB)$'
    match = re.match(patron, genero)
    
    if match:
        genero_valido = match.group(1)
        primer_numero = '1' if genero_valido == 'M' else '2' if genero_valido == 'F' else '0'
        
        # Genera el código con ceros a la izquierda
        codigo = f"{genero_valido}-{primer_numero}{str(id).zfill(7)}"

        if len(primer_numero) < 10:
            return codigo

    return 'N/A'
"""
2.2. Crear la función ‘stark_generar_codigos_heroes’  la cual recibirá como parametro:
    • lista_heroes: la lista de personajes:
La función deberá iterar la lista de personajes y generar cada uno de los códigos
El código del héroe (id_heroe) surge de la posición del mismo dentro de la lista_heroes (comenzando por el 1).
Reutilizar la función anterior pasándole como argumentos el id_heroe correspondiente
Guardar en un string cada uno de los heroes con el siguiente formato y al final de toda la iteración debería quedar un mensaje como el siguiente ejemplo
* howard_the_duck (H.W.) | M-10000001
* rocket_raccoon (R.R.) | NB-0000002
		* wolverine (W.) |  M-10000003
		* black_widow (B.W.) | F-20000004
………
Se asignaron ## códigos 
En donde ## es la cantidad de códigos que se generaron
La función deberá validar::
    • La lista contenga al menos un elemento
    • Todos los elementos de la lista sean del tipo diccionario

	La función retornara la cadena generada si salió todo correctamente y False en caso de error
"""
def stark_generar_codigos_heroes(lista_heroes):
    # Validar que la lista contenga al menos un elemento
    if not lista_heroes:
        return False

    # Validar que todos los elementos de la lista sean diccionarios
    if not all(isinstance(heroe, dict) for heroe in lista_heroes):
        return False
    # Generar códigos para cada héroe e imprimirlos
    resultado = ""
    contador = 0
    for i, heroe in enumerate(lista_heroes, start=1):
        id_heroe = str(i)
        codigo = generar_codigo_heroe(heroe, id_heroe)
        nombres = stark_imprimir_nombre_con_iniciales(heroe)
        if codigo != "N/A":
            resultado += f"* {nombres} | {codigo}\n"
            contador += 1

    if contador > 0:
        print(resultado)
    else:
        return False
"""
3.1. Crear la función ‘sanitizar_entero’ la cual recibirá como parámetro:
    • numero_str: un string que representa un posible número entero
La función deberá analizar el string recibido y determinar si es un número entero positivo.  La función debe devolver distintos valores según el problema encontrado:
    • Si contiene carácteres no numéricos retornar -1
    • Si el número es negativo se deberá retornar un -2
    • Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3
También deberá quitar los espacios en blanco de atras y adelante del string en caso que los tuviese
En caso que se verifique que el texto contenido en el string es un número entero positivo, retornarlo convertido en entero
"""
def sanitizar_entero(numero_str):
    numero_str = numero_str.strip()
    patron_numero = r'^\d+$'
    try:
        if re.match(patron_numero, numero_str):
            numero = int(numero_str)
            if numero >= 0:
                return numero
            else:
                return False 
        else:
            return True
    except ValueError:
        return False 
"""
3.2. Crear la función ‘sanitizar_flotante’ la cual recibirá como parámetro:
    • numero_str: un string que representa un posible número decimal
La función deberá analizar el string recibido y determinar si es un número flotante positivo.  La función debe devolver distintos valores según el problema encontrado:
    • Si contiene carácteres no numéricos retornar -1
    • Si el número es negativo se deberá retornar un -2
    • Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3
También deberá quitar los espacios en blanco de atras y adelante del string en caso que los tuviese
En caso que se verifique que el texto contenido en el string es un número flotante positivo, retornarlo convertido en flotante
"""
def sanitizar_flotante(numero_str):
    numero_str = numero_str.strip()
    patron_numero = r'^\d+(\.\d+)?$'
    try:
        if re.match(patron_numero, numero_str):
            numero = float(numero_str)
            if numero >= 0:
                return numero
            else:
                return -2  
        else:
            return -1 
    except ValueError:
        return -3  
"""
3.3. Crear la función ‘sanitizar_string’’ la cual recibirá como parámetro
    • valor_str: un string que representa el texto a validar
    • valor_por_defecto: un string que representa un valor por defecto (parámetro opcional, inicializarlo con ‘-’)
La función deberá analizar el string recibido y determinar si es solo texto (sin números). En caso de encontrarse números retornar “N/A”
En el caso que valor_str contenga una barra ‘/’ deberá ser reemplazada por un espacio
	El espacio es un caracter válido 
En caso que se verifique que el parámetro recibido es solo texto, se deberá retornar el mismo convertido todo a minúsculas
En el caso que el texto a validar se encuentre vacío y que nos hayan pasado un valor por defecto, entonces retornar el valor por defecto convertido a minúsculas
Quitar los espacios en blanco de atras y adelante de ambos parámetros en caso que los tuviese
"""
def sanitizar_string(valor_str, valor_por_defecto='-'):
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()
    patron_numeros = r'\d+'
    if re.search(patron_numeros, valor_str):
        return "N/A"  
    valor_str = re.sub(r'/', ' ', valor_str)
    if not valor_str and valor_por_defecto:
        return valor_por_defecto.lower()
    if re.match(r'^[A-Za-z\s]+$', valor_str):
        return valor_str.lower()
    return "N/A" 
"""
3.4. Crear la función ‘sanitizar_dato’ la cual recibirá como parámetros:
    • heroe: un diccionario con los datos del personaje
    • clave: un string que representa el dato a sanitizar (la clave del diccionario). Por ejemplo altura
    • tipo_dato: un string que representa el tipo de dato a sanitizar. Puede tomar los valores: ‘string’, ‘entero’ y ‘flotante’
La función deberá sanitizar el valor del diccionario correspondiente a la clave y al tipo de dato recibido
Para sanitizar los valores se deberán utilizar las funciones creadas en los puntos 3.1, 3.2, 3.3 y 3.4

Se deberá validar:
    • Que tipo_dato se encuentre entre los valores esperados (‘string, ‘entero, ‘flotante)’ la validación debe soportar que nos lleguen mayúsculas o minúsculas. En caso de encontrarse un valor no válido informar por pantalla: ‘Tipo de dato no reconocido’

    • Que clave exista como clave dentro del diccionario heroe. En caso de no encontrarse, informar	 por pantalla: ‘La clave especificada no existe en el héroe’. (en este caso la validación es sensible a mayúsculas o minúsculas) 
	Ejemplo de llamada a la función válida:
sanitizar_dato(dict_personaje, “altura”, “Flotante”)
La función deberá devolver True en caso de haber sanitizado algún dato y False en caso contrario.
"""
def sanitizar_dato(lista, clave, tipo_dato):
    lista_copiada = copy.deepcopy(lista)
    tipo_dato = tipo_dato.lower()
    se_realizo_sanitizacion = False
    for heroe in lista_copiada:
        if clave in heroe:
            dato_a_sanitizar = heroe[clave]
            if tipo_dato == "flotante":
                heroe[clave] = sanitizar_flotante(dato_a_sanitizar)
                se_realizo_sanitizacion = True
            elif tipo_dato == "entero":
                heroe[clave] = sanitizar_entero(dato_a_sanitizar)
                se_realizo_sanitizacion = True
            elif tipo_dato == "string":
                heroe[clave] = sanitizar_string(dato_a_sanitizar, valor_por_defecto='-')
                se_realizo_sanitizacion = True
    
    if se_realizo_sanitizacion:
        return heroe[clave]
    else:
        print(f'La clave "{clave}" no existe en ningún héroe o el tipo de dato no es válido: "{tipo_dato}"')
        return False
"""
3.5. Crear la función 'stark_normalizar_datos’ la cual recibirá como parámetros:
    • lista_heroes: la listas personajes
La función deberá recorrer la lista de héroes y sanitizar los valores solo de las siguientes claves: ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e ‘inteligencia’
    • Un vez finalizado el proceso mostrar el mensaje ‘Datos normalizados’, 
    • Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
    • La función no retorna nada
    • Reutilizar la función sanitizar_dato
"""
def stark_normalizar_datos(lista):
    lista_copiada = copy.deepcopy(lista)
    if len(lista_copiada) > 0:
        sanitizar_dato(lista_copiada,"altura", "flotante")
        sanitizar_dato(lista_copiada,"peso", "flotante")
        sanitizar_dato(lista_copiada,"color_ojos", "string")
        sanitizar_dato(lista_copiada,"color_pelo", "string")
        sanitizar_dato(lista_copiada,"fuerza", "entero")
        sanitizar_dato(lista_copiada,"inteligencia", "entero")
        return lista_copiada
"""
4.1. Crear la función ‘stark_imprimir_indice_nombre’ la cual recibirá como parámetro:
    • lista_heroes: la lista de personajes
La función deberá mostrar por pantalla cada una de las palabras de cada uno de los nombres que existan en el data_stark separado por un guion entre cada una de las palabras ignorando las palabras que digan “the” -> (Usar regex)
Por ejemplo:
Howard-duck-Rocket-Raccoon-Wolverine…
Usar alguna de las funciones vistas en la PPT strings
"""
def stark_imprimir_indice_nombre(lista):
    lista_copiada = copy.deepcopy(lista)
    nombres_concatenados = ""
    patron_the = r'\bthe\b'
    for heroe in lista_copiada:
        if 'nombre' in heroe:
            nombre = heroe['nombre']
            nombre_formateado = re.sub(patron_the, '', nombre, flags=re.IGNORECASE)
            nombre_formateado = re.sub(r'\s+', '-', nombre_formateado).strip('-')
            nombres_concatenados += nombre_formateado + '-'
    nombres_concatenados = nombres_concatenados.rstrip('-')
    print(nombres_concatenados)
"""
5.1 Crear la función ‘generar_separador’ la cual recibirá como parámetro
    • patron: un carácter que se utilizará como patrón para generar el separador
    • largo: un número que representa la cantidad de caracteres que va ocupar el separador.
    • imprimir: un parámetro opcional del tipo booleano (por default definir en True) 
La función deberá generar un string que contenga el patrón especificado repitiendo tantas veces como la cantidad recibida como parámetro (uno junto al otro, sin salto de línea)
Si el parámetro booleano recibido se encuentra en False se deberá solo retornar el separador generado. Si se encuentra en True antes de retornarlo, imprimirlo por pantalla
La función deberá validar: 
    • Que el parámetro patrón tenga al menos un carácter y como máximo dos
    • Que el parámetro largo sea un entero entre 1 y 235 inclusive
En caso de no verificarse las validaciones devolver ‘N/A’
Ejemplo de llamada:
generar_separador(‘*’, 10)
Ejemplo de salida:
**********
"""
def generar_separador(patron, largo, imprimir=True):
    if not (1 <= len(patron) <= 2):
        return 'N/A'
    
    if not (1 <= largo <= 235):
        return 'N/A'

    separador = patron * largo

    if imprimir:
        print(separador)
    else:
        return separador
"""
5.2 Crear la función ‘generar_encabezado’ la cual recibirá como parámetro
    • titulo: un string que representa el título de una sección de la ficha
La función deberá devolver un string que contenga el título envuelto entre dos separadores (estimar el largo requerido para tu pantalla). 
Ejemplo de salida:
********************************************************************************
PRINCIPAL
********************************************************************************
La función deberá convertir el titulo recibido en todas letras mayúsculas
"""
def generar_encabezado(titulo):
    titulo_mayuscula = titulo.upper()
    generar_separador('*', 150)
    print(titulo_mayuscula)
    generar_separador('*', 150)
"""
5.3	Crear la función ‘imprimir_ficha_heroe’ la cual recibirá como parámetro:
    • heroe: un diccionario con los datos del héroe
La función deberá a partir los datos del héroe generar un string con el siguiente formato e imprimirlo por pantalla::
***************************************************************************************
PRINCIPAL
***************************************************************************************
NOMBRE DEL HÉROE: 			spider_man (S.M.)
IDENTIDAD SECRETA:			peter_parker
CONSULTORA:				marverl_comics
CÓDIGO DE HÉROE	:			M-10000001
***************************************************************************************
FISICO
***************************************************************************************
ALTURA: 					178 cm.
PESO:						74,25 kg.
FUERZA: 					55 N
***************************************************************************************
SEÑAS PARTICULARES
***************************************************************************************
	COLOR DE OJOS:				Hazel
	COLOR DE PELO:				Brown

Recordatorio: Se pueden usar índices negativos si desean
"""
def imprimir_ficha_heroe(heroe):
    if isinstance(heroe, dict):
        heroe_nombre = obtener_dato_formato(heroe['nombre'])
        heroe_iniciales = extraer_iniciales(heroe['nombre'])
        heroe_identidad = obtener_dato_formato(heroe['identidad'])
        heroe_consultora = obtener_dato_formato(heroe['empresa'])
        heroe_codigo = generar_codigo_heroe(heroe, 1)
        heroe_altura = sanitizar_flotante(heroe['altura'])
        heroe_peso = sanitizar_flotante(heroe['peso'])
        generar_encabezado("principal")
        print("NOMBRE DEL HÉROE: 			"+heroe_nombre+f" ({heroe_iniciales})")
        print("IDENTIDAD SECRETA:			"+heroe_identidad)
        print("CONSULTORA:				"+heroe_consultora)
        print("CÓDIGO DE HÉROE	:			"+heroe_codigo)
        generar_encabezado("fisico")
        print("ALTURA: 					"+str(heroe_altura)+" cm.")
        print("PESO:						"+str(heroe_peso)+" kg.")
        print("FUERZA: 					"+heroe['fuerza']+" N")
        generar_encabezado("señas particulares")
        print("COLOR DE OJOS:				"+heroe['color_ojos'])
        print("COLOR DE PELO:				"+heroe['color_pelo'])
"""
    5.5. Crear la función 'stark_navegar_fichas’ la cual recibirá como parámetros:
    • lista_heroes: la listas personajes
La función deberá comenzar imprimiendo la ficha del primer personaje de la lista y luego solicitar al usuario que ingrese alguna de las siguientes opciones:
[ 1 ] Ir a la izquierda 		[ 2 ] Ir a la derecha 		[ 3 ] Salir
    • Si el usuario ingresa ‘1’: se debe mostrar el héroe que se encuentra en la posición anterior en la lista  (en caso de estar en el primero, ir al último)

    • Si el usuario ingresa ‘2’:  se debe mostrar el héroe que se encuentra en la posición siguiente en la lista (en caso de estar en el último, ir al primero)

    • Si ingresa 3: volver al menú principal

    • Si ingresa cualquier otro valor, volver a mostrar las opciones hasta que ingrese un valor válido
"""
def stark_navegar_fichas(lista_heroes):
    if not lista_heroes:
        print("La lista de héroes está vacía.")
        return

    i = 0
    catalogo = len(lista_heroes)

    while True:
        # Imprimir la ficha del héroe en la posición actual
        imprimir_ficha_heroe(lista_heroes[i])

        # Solicitar al usuario que ingrese una opción
        opcion = input("Ingresa una opción: [1] Izquierda, [2] Derecha, [3] Salir: ")

        if opcion == '1':
            # Retroceder en la lista (ir a la izquierda)
            i -= 1
            if i < 0:
                i = catalogo - 1
        elif opcion == '2':
            # Avanzar en la lista (ir a la derecha)
            i += 1
            if i >= catalogo:
                i = 0
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Ingresa '1', '2' o '3'.")

############################Ejercicio Stark 05#############################################
"""
1. Primera Parte: Archivos
1.1. Crear la función 'leer_archivo' la cual recibirá por parámetro un string
que indicará el nombre y extensión del archivo a leer (Ejemplo:
archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
retornara un string con la información del mismo.
ATENCIÓN:Controlar las excepciones posibles en caso de
presentarse alguna imprimir el mensaje de la misma y retornar
False
Usar de Encoding UTF-8
"""
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Error: {e}")
    return False

"""
1.2. Crear la función 'guardar_archivo' la cual recibirá por parámetro un
string que indicará el nombre con el cual se guardará el archivo junto
con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro
tendrá un string el cual será el contenido a guardar en dicho archivo.
Debe abrirse el archivo en modo escritura+, ya que en caso de no
existir, lo creara y en caso de existir, lo va a sobreescribir La función
debera retornar True si no hubo errores, caso contrario False
(VALIDAR CON EXCEPCIONES), además en caso de éxito, deberá
imprimir un mensaje respetando el formato:
Se creó el archivo: nombre_archivo.csv
ATENCIÓN:Controlar las excepciones posibles en caso de
presentarse alguna retornar false e imprimir un mensaje que
diga:: ‘Error al crear el archivo: nombre_archivo’
Donde nombre_archivo será el nombre que recibirá el archivo a
ser creado, conjuntamente con su extensión.
Usar de Encoding UTF-8
"""
def guardar_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'w+', encoding='utf-8') as archivo:
            archivo.write(contenido)
            print(f"Se creó el archivo: {nombre_archivo}")
            return True
    except Exception as e:
        print(f"Error al crear el archivo: {nombre_archivo}")
        print(f"Detalle del error: {e}")
    return False


"""
1.3. Crear la función generar_csv()
La función va a recibir el nombre y extensión del archivo csv de los
superhéroes (Puede ser ruta absoluta o relativa) y la lista de los
mismos.
Si la lista no está vacía la función deberá guardar en un string la
información en formato csv (separado con comas) con la cabecera
correspondiente.
Una vez generado el string debería usar la función de 1.2 para guardar
ese string generado al archivo.
Si la lista está vacia retornar False
"""
def generar_csv(nombre_archivo, lista_superheroes):
    if not lista_superheroes:
        print("La lista de superhéroes está vacía.")
        return False

    # Generar el contenido CSV
    contenido_csv = "Nombre,Identidad,Empresa,Altura,Peso,Género,Color de Ojos,Color de Pelo,Fuerza,Inteligencia\n"  # Cabecera

    for superheroe in lista_superheroes:
        contenido_csv += f"{superheroe['nombre']},{superheroe['identidad']},{superheroe['empresa']},{superheroe['altura']},{superheroe['peso']},{superheroe['genero']},{superheroe['color_ojos']},{superheroe['color_pelo']},{superheroe['fuerza']},{superheroe['inteligencia']}\n"

    # Guardar el contenido en el archivo usando la función de 1.2
    exito = guardar_archivo(nombre_archivo, contenido_csv)

    return exito


"""
1.4. Crear la función leer_csv() que va a recibir el nombre y extensión de
donde se ubica el archivo a leer (Ruta absoluta o relativa)
La función se tiene que encargar de generar una lista de superhéroes
en base al contenido de ese archivo csv que se le paso. Pueden usar
la cabecera de ese csv para generar las claves de cada uno de los
diccionarios.
La función debe retornar la lista de diccionarios si es que existe el
archivo y sino False.    
"""
def leer_csv(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            lista_superheroes = [dict(fila) for fila in csv_reader]

        return lista_superheroes

    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado.")
        return False
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return False


"""
1.5. Crear la función generar_json() que va a recibir el nombre y extensión
de donde se ubica el archivo a guardar (Ruta absoluta o relativa) , la
lista de los superhéroes y el nombre de la lista.
Si la lista no está vacía debería guardar en un diccionario de una sóla
clave la lista de superhéroes,el nombre de clave debería ser la del
tercer parámetro que sería el nombre de la lista.
ATENCIÓN:Usar indent=4 al generar el Json
También tener en cuenta que los datos deben estar normalizados
antes de generar el json.
"""
def generar_json(nombre_archivo, lista_superheroes, nombre_lista):
    try:
        if lista_superheroes:
            datos = {nombre_lista: lista_superheroes}

            with open(nombre_archivo, 'w', encoding='utf-8') as file:
                json.dump(datos, file, indent=4)

            print(f"Se creó el archivo: {nombre_archivo}")
            return True
        else:
            print("La lista de superhéroes está vacía. No se generó el archivo JSON.")
            return False
    except Exception as e:
        print(f"Error al generar el archivo JSON: {e}")
        return False

"""
1.6. Crear la función leer_json() que va a recibir el nombre y extensión de
donde se ubica el archivo a leer (Ruta absoluta o relativa), y también el
nombre de la lista a leer por ejemplo en la imagen anterior la lista está
en la clave “heroes”
Si el archivo existe deberia leer el archivo json y retornar la lista
obtenida.
Si el achivo no existe deberia retornar False (USAR EXCEPCIONES)
"""
def leer_json(nombre_archivo, nombre_lista):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            datos = json.load(file)

            if nombre_lista in datos:
                return datos[nombre_lista]
            else:
                print(f"La clave {nombre_lista} no existe en el archivo JSON.")
                return False
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return False
    except Exception as e:
        print(f"Error al leer el archivo JSON: {e}")
        return False

"""
2.1. Crear una función para ordenar héroes por alguna de las claves
númericas (altura, peso y fuerza) de manera ascendente
"""
def ordenar_heroes_ascendentes(lista_superheroes, clave_orden):
    try:
        # Verificar si la clave de orden existe en al menos un héroe
        if clave_orden not in lista_superheroes[0]:
            print(f"La clave de orden '{clave_orden}' no existe en los datos de los superhéroes.")
            return None

        # Realizar una copia profunda de la lista para no alterar la original
        lista_superheroes_copia = copy.deepcopy(lista_superheroes)

        # Ordenar la lista de superhéroes copiada por la clave especificada
        n = len(lista_superheroes_copia)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if float(lista_superheroes_copia[j][clave_orden]) > float(lista_superheroes_copia[j + 1][clave_orden]):
                    lista_superheroes_copia[j], lista_superheroes_copia[j + 1] = (
                        lista_superheroes_copia[j + 1],
                        lista_superheroes_copia[j]
                    )

        return lista_superheroes_copia

    except IndexError:
        print("La lista de superhéroes está vacía.")
        return None
    except ValueError:
        print(f"Error al ordenar por la clave '{clave_orden}'. Asegúrate de que los valores sean numéricos.")
        return None


"""
2.2. Crear una función para ordenar héroes por alguna de las claves
númericas (altura, peso y fuerza) de manera descendente.
"""
def ordenar_descendente(lista_superheroes, clave_orden):
    try:
        # Verificar si la clave de orden existe en al menos un héroe
        if clave_orden not in lista_superheroes[0]:
            print(f"La clave de orden '{clave_orden}' no existe en los datos de los superhéroes.")
            return None

        # Implementación del método de burbujeo descendente
        n = len(lista_superheroes)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if lista_superheroes[j][clave_orden] < lista_superheroes[j + 1][clave_orden]:
                    lista_superheroes[j], lista_superheroes[j + 1] = lista_superheroes[j + 1], lista_superheroes[j]

        return lista_superheroes

    except IndexError:
        print("La lista de superhéroes está vacía.")
        return None
    except ValueError:
        print(f"Error al ordenar por la clave '{clave_orden}'. Asegúrate de que los valores sean numéricos.")
        return None

"""
2.3. Crear una función para ordenar héroes por alguna de las claves
númericas (altura, peso y fuerza). Preguntar al usuario si lo quiere
ordenar de manera ascendente (‘asc’) o descendente (‘desc’) (reutilizar
funciones anteriores dependiendo del caso)
"""
def ordenar_heroes_por_clave(lista_superheroes, clave_orden):
    try:
        # Verificar si la clave de orden existe en al menos un héroe
        if clave_orden not in lista_superheroes[0]:
            print(f"La clave de orden '{clave_orden}' no existe en los datos de los superhéroes.")
            return None

        # Preguntar al usuario si quiere ordenar de manera ascendente ('asc') o descendente ('desc')
        orden = input("¿Cómo quieres ordenar los héroes? ('1' para ascendente, '2' para descendente): ")
        if orden not in ['1', '2']:
            print("Opción no válida. Debes elegir '1' o '2'.")
            return None

        # Llamar a la función correspondiente según la elección del usuario
        if orden == '1':
            return ordenar_heroes_ascendentes(lista_superheroes, clave_orden)
        elif orden == '2':
            return ordenar_descendente(lista_superheroes, clave_orden)

    except IndexError:
        print("La lista de superhéroes está vacía.")
        return None

"""
funcion para normalizar los datos
"""
def convertir_datos(lista_personajes):
    for personaje in lista_personajes:
        # Convertir altura y peso a float
        personaje['altura'] = float(personaje['altura'])
        personaje['peso'] = float(personaje['peso'])

        # Convertir fuerza e inteligencia a int si no están vacíos
        if personaje['fuerza']:
            personaje['fuerza'] = int(personaje['fuerza'])


    return lista_personajes