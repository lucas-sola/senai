#-*- coding:UTF-8 -*-
a = int(input("diga aqui diga aqui dois valores e eu direi o maior deles"))
b = int(input("Diga aqui o segundo valor para eu dizer o maior!"))

def maiornumero(a, b):
    if a > b:
        return (f"{a} é maior que {b}")
    else:
        return (f"{b} é maior que {a}")



