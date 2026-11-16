alumnos = {
    "Ana": (18, 17),
    "Luis": (14, 19),
    "Mía": (20, 16),
    "Carlos": (12,15),
    "Eva": (17, 18),
    "Noah": (15, 20)
}
promedios_alumnos = {}
promedio_generale = 0
# índice 0 Matemáticas, Índice 1 Programación
def promedios(lista):
    for alumno, notas in lista.items():
        promedio = (notas[0] + notas[1]) / 2
        if alumno not in promedios_alumnos:
            promedios_alumnos[alumno] = promedio
            print(alumno,":", promedio)
    return promedios_alumnos
resultado = promedios(alumnos)
print(resultado)
def encontrar_promedio(lista):
    mayor_promedio = 0
    alumno_mayor = ""
    for alumno, promedio in lista.items():
        if promedio > mayor_promedio:
            mayor_promedio = promedio
            alumno_mayor = alumno
    return alumno_mayor, mayor_promedio
resultado2 = encontrar_promedio(promedios_alumnos)
print(resultado2)
def promedio_general(lista):
    acumulador = 0
    for nombre, promedio in lista.items():
        acumulador += lista[nombre]
    average = (acumulador) / len(lista)
    return average
promedio_generale = promedio_general(promedios_alumnos)
print(promedio_generale)