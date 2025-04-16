#-*- coding: UTF-8 -*-

valor = 0 

def primo():
    valor = int(input("diga o valor que você quer ver se é primo, que seja INTEIRO! "))
    if valor <= 1:
        print("digite um número valido!")
    elif valor == 2:
        for x in range(2, valor, +1):
            if valor % x == 0:
                print("nao é primo")
                break
            elif valor % x != 0:
                print("é primo")
                break
    else:
        for x in range(2, valor):
            if valor % x == 0:
                print("nao é primo")
                break
            elif valor % x != 0:
                print("é primo")
                break
    
primo()
