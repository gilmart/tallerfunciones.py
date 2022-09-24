numeros=[]

def llenarArreglo(numeros):
    for suma in range(5): 
        numero=int(input(f'Digite un numero: {suma+1} '))
        numeros.append(numero)

llenarArreglo(numeros)
print(numeros)

