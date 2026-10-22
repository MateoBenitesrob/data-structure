numeros = [5, 2, 5, 8, 2, 5, 9, 2, 2]
diccionario = {}
contador_alto = 0
nvmero = 0
for numero in numeros:
    if numero not in diccionario:
        diccionario[numero] = 1
    else:
        diccionario[numero] += 1
    if diccionario[numero] > contador_alto:
        contador_alto = diccionario[numero]
        nvmero = numero
print(nvmero, diccionario[nvmero])