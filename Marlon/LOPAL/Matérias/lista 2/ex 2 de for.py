#-*- coding: UTF-8 -*-

#o codigo dira a soma dos 50 primeiros números pares

acum = 0 
for i in range (0, 101): 
    if i % 2 == 0:
        acum = acum + i
        print("A soma dos pares é:", acum)
