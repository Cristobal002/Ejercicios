# 1. Contar Ocurrencias de Elementos
def contarOcurrencias(palabras):

    resultado={}

    for palabra in palabras:
        if palabra in resultado:
            resultado[palabra] += 1
        else:
            resultado[palabra] = 1
    return resultado

# Ejemplo
palabras = ["nazi", "java", "nazi", "gays", "libro", "casa"]
print("Resultado del ejercicio #1\n", contarOcurrencias(palabras))

# 2. Combinar Diccionarios
def combinarDiccionarios(dic1, dic2):

    resultado = dic1.copy()

    for clave, valor in dic2.items():
        if clave in resultado:
            resultado[clave] += valor
        else:
            resultado[clave] = valor
    return resultado

# Ejemplo
dic1 = {'A': 1, 'B': 2}
dic2 = {'C': 3, 'D': 4}
print("Resultado del ejercicio #2\n", combinarDiccionarios(dic1, dic2))

# 3. Listas de Frecuencia
def frecuenciaDeNumeros(numeros):

    resultado = {}

    for numero in numeros:
        if numero in resultado:
            resultado[numero] += 1
        else:
            resultado[numero] = 1
    return resultado

# Ejemplo
numeros = [1, 1, 2, 3, 3, 3]
print("Resultado del ejercicio #3\n", frecuenciaDeNumeros(numeros))

# 4. Filtrar Palabras Largas
def filtrarPalabrasLargas(palabras, longitud):
    return [palabra for palabra in palabras if len(palabra) > longitud]

# Ejemplo
palabras = ["hitler", "ayasaka", "miku", "yuno_gasai"]
longitud = 9
print("Resultado del ejercicio #4\n", filtrarPalabrasLargas(palabras, longitud))

# 5. Inversión de Tuplas en Lista
def invertirNumeros(tuplas):
    return [(n2, n1) for n1, n2 in tuplas]

# Ejemplo
tuplas = [(1, 2), (3, 4), (5, 6)]
print("Resultado del ejercicio #5\n", invertirNumeros(tuplas))

# 6. Encontrar el Valor Más Frecuente
def valorMasFrecuente(numeros):
    frecuencia = frecuenciaDeNumeros(numeros)
    return max(frecuencia, key=frecuencia.get)

# Ejemplo
numeros = [1, 2, 3, 1, 2, 1]
print("Resultado del ejercicio #6\n", "El valor mas frecuente es : ", valorMasFrecuente(numeros))

# 7. Comprobar Subconjunto
def esSubconjunto(conjunto1, conjunto2):
    return conjunto1.issubset(conjunto2)

# Ejemplo
conjunto1 = {1, 2, 3}
conjunto2 = {1, 2, 3, 4, 5}
print("Resultado del ejercicio #7\n", esSubconjunto(conjunto1, conjunto2))

# 8. Agrupación por Clave
def agruparPorEdad(personas):

    agrupacion = {}

    for persona in personas:
        edad = persona['edad']
        if edad not in agrupacion:
            agrupacion[edad] = []
        agrupacion[edad].append(persona['nombre'])
    return agrupacion

# Ejemplo
personas = [{"nombre": "Ana", "edad": 25}, {"nombre": "Luis", "edad": 25}, {"nombre": "Carlos", "edad": 30}]
print("Resultado del ejercicio #8\n", agruparPorEdad(personas))

# 9. Merge Sort utilizando Listas
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda, derecha = merge_sort(lista[:medio]), merge_sort(lista[medio:])
    return sorted(izquierda + derecha)

# Ejemplo
numeros = [5, 3, 8, 6, 2]
print(merge_sort(numeros))

# 10. Eliminar Elementos por Condición
def eliminarNumerosMenores(numeros, limite):
    return [num for num in numeros if num >= limite]

# Ejemplo
numeros = [1, 2, 3, 4, 5]
limite = 3
print("Resultado del ejercicio #10\n", eliminarNumerosMenores(numeros, limite))

# 11. Flatten List of Lists
def aplanarLista(lista_de_listas):
    return [elemento for sublista in lista_de_listas for elemento in sublista]

# Ejemplo
lista_de_listas = [[1, 2], [3, 4], [5]]
print("Resultado del ejercicio #11\n", aplanarLista(lista_de_listas))  # [1, 2, 3, 4, 5]

# 12. Cálculo de Mediana
def calcularMediana(numeros):

    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    medio = n // 2

    if n % 2 == 0:
        return (numeros_ordenados[medio - 1] + numeros_ordenados[medio]) / 2
    else:
        return numeros_ordenados[medio]

# Ejemplo
numeros = [1, 3, 2, 4, 5]
print("Resultados del ejercicio #12\n", calcularMediana(numeros))

# 13. Duplicar Elementos en una Lista
def duplicarElementos(numeros):
    return [num for num in numeros for _ in range(2)]

# Ejemplo
numeros = [1, 2, 3]
print("Resultados del ejercicio #13\n", duplicarElementos(numeros))

# 14. Contar Palabras en Frases
def contarPalabras(frases):
    return {i: len(frase.split()) for i, frase in enumerate(frases)}

# Ejemplo
frases = ["Hola mundo", "Python es genial", "Me gusta programar"]
print("Resultados del ejercicio #14\n", contarPalabras(frases))

# 15. Encontrar Clave Máxima en Diccionario
def claveMaxima(diccionario):
    return max(diccionario, key=diccionario.get)

# Ejemplo
diccionario = {'a': 10, 'b': 20, 'c': 5}
print("Resultados del ejercicio #15\n", claveMaxima(diccionario))

# 16. Palíndromos en una Lista
def encontrarpalindromos(palabras):
    return [palabra for palabra in palabras if palabra == palabra[::-1]]

# Ejemplo
palabras = ["ana", "oso", "hola", "level"]
print("Resultados del ejercicio #16\n", encontrarpalindromos(palabras))