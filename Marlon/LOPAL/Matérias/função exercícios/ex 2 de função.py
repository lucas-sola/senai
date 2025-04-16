#-*- coding: UTF-8 -*-

#
#Faça um programa com uma função que receba dois
#números e retorne True se o primeiro número for
#múltiplo do segundo.

n1 = int(input("diga aqui dois valores para eu dizer se o primeiro valor é múltiplo do segundo"))
n2 = int(input("diga aqui dois valores para eu dizer se o primeiro valor é múltiplo do segundo"))

def multiplos(n1, n2):
    if n2 % n1 == 0:
        return True
    else:
        return False
    
print(multiplos(n1, n2))
