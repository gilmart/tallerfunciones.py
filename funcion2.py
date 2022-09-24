def calcularArea(w,h):
    area= (w*h)/2
    return(area)

w=int(input(f'digite el ancho '))
h=int(input(f'digite el alto '))

print(calcularArea(w,h))


def calcularPerimetro():
    print()


def calcularPerimetro(w, h):
    perimetro = (2*w) + (2*h)
    return perimetro
    

print(f'El perimetro es: { calcularPerimetro(w, h) }')

def graficar(w, h):
    for pintar in range(h): 
        print(w*'*')


graficar(w,h)
