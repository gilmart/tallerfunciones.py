numeros=[]

def llenarArreglo(numeros):
    for suma in range(5): 
        numero=int(input(f'Digite un numero: {suma+1} '))
        numeros.append(numero)

llenarArreglo(numeros)
print(numeros)


def sumarArreglo(numeros):
    contador=0
    for suma in numeros:
        contador=contador+suma
    return contador

print (sumarArreglo(numeros))

sumaArray = sumarArreglo(numeros)

def calcularPromedio(suma):
    longitud = suma  / len(numeros)
    return longitud


print(f'El promedio de los valores del vector es: { calcularPromedio(sumaArray) }')
