#-*- coding: UTF-8 -*-

valor = 0

def tabuada(valor):
    valor = int(input("Diga aqui o valor que você quer a tabuada! "))
    for x in range(1, 11):
        print(f"{valor} * {x} = {valor * x}")

tabuada(valor)