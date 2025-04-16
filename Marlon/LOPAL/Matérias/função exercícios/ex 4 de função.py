#-*- coding: UTF-8 -*-

#Faça um programa com uma função que receba a base e a altura de um triângulo e retorne a sua área (A = (basex altura) / 2).

base = float(input("Diga aqui o valor da base de um triangulo para eu calcular sua área"))
altura = float(input("Diga aqui o valor da altura de um triangulo para eu calcular sua área"))

def area(base, altura):
    return (base * altura) / 2

print(area(base, altura)) 