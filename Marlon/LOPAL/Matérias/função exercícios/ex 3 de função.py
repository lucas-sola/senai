#-*- coding: UTF-8 -*-

#Faça um programa com uma função que receba o lado (l) de um quadrado e retorne a sua área (A = lado2).

l = float(input("Diga aqui o valor do lado de um quadrado e eu retornarei sua área! "))

def area(l):
    return l * l
print(area(l))