A = [4, 7, 4, 9, 2, 7, 4]
B = [7, 4, 7, 1, 4, 7, 8]
diccionario1 = {}
diccionario2 = {}
diccionario3 = {}
for num1 in A:
    if num1 not in diccionario1:
        diccionario1[num1] = 1
    else:
        diccionario1[num1] += 1
for num2 in B:
    if num2 not in diccionario2:
        diccionario2[num2] = 1
    else:
        diccionario2[num2] += 1
for recorrer in diccionario1:
     if recorrer in diccionario2:
          diccionario3[recorrer] = diccionario1[recorrer], diccionario2[recorrer]
print(diccionario3)