#-*- coding: UTF-8 -*-

#codigo para mostrar os números divisores de outro

n = int(input("Diga aqui um valor"))
for x in range (1, n+1):
    if n % x == 0:
        print(x)
