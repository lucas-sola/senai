#-*- coding: UTF-8 -*- 

raio = float(input("diga aqui o valor do raio de um círculo e eu direi sua área" ))
pi = 3.14
def area(raio):
    return pi * (raio * raio)

print (area(raio))