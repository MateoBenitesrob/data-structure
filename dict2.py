numeros = [4, 7, 4, 2, 7, 4, 9, 2, 7, 7]
diccionario = {}
contador = 0
for numero in numeros:
    if numero not in diccionario:
        diccionario[numero] = 1
    else:
        diccionario[numero] += 1
print(diccionario)
