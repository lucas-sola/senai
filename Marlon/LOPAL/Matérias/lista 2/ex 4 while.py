#-*- coding: UTF-8 -*-

#codigo para ver os valores pares e impares que o usuario colocou

valor_impar = 0
valor_par = 0

while True:
    num = int(input("Diga-me um valor, digite um valor negativo para sair"))
    if num < 0:
        print("Você escolheu sair, tchau!")
        break
    if num % 2 == 0:
        valor_par = valor_par + 1 
    else:
        valor_impar = valor_impar + 1
print(f"valor par = {valor_par} e valor impar = {valor_impar}")
