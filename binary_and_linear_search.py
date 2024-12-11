import time
import random

print("creando la lista")
lista_aleatoria = random.sample(range(1, 100000000), 10000000)
print("ordenando la lista")
lista_aleatoria.sort()
print("buscando elemntos")

def buscar_bi(lista, numero):
    ini = 0
    fin = len(lista) - 1
    while ini <= fin:
        puntero = (ini + fin)//2
        if lista[puntero] == numero:
            return puntero
        elif lista[puntero] < numero:
            ini = puntero + 1
        else:
            fin = puntero -1
    return "numero no encotrada"



def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return "numero no encontrado"


def calculo(funcion):
    ini = time.time()
    for i in range(10):
        num = random.randint(1, 100000000)
        funcion(lista_aleatoria,num)
    fin = time.time()
    return fin - ini

print("busqueda bi: ",calculo(buscar_bi))
print("busqueda lineal: ",calculo(busqueda_lineal))