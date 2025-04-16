#-*- coding: UTF-8 -*-


print("Olá, este programa irá calcular a soma de todos os números até ele. Ou seja, caso você coloque o número 3, 1 + 2 + 3!")

v = int(input("diga aqui o valor de um número inteiro e eu calcularei a soma de todos os números até ele>"))
cont = 0

if v < 0:
    print("Coloque um número válido!")
else:
    for x in range(1, v):
        cont = cont + x 
        print(f"os valores são: = {cont}")
    
