    #-*- coding: UTF-8 -*-

n1 = float(input("Diga um numero"))
n2 = float(input("Diga outro numero"))

soma = n1 + n2
divisao = n1 / n2
subtracao = n1 - n2
multiplicacao = n1 * n2

operacao = print("qual operação você deseja utilizar? lembre-se de escrever sem acentos e a primeira letra minúscula!  ")

if operacao == "soma":
    print("A soma dos dois números é:", soma)
elif operacao == "divisão":
    print("Voce selecionou a divisão, seu resultado é:", divisao)
elif operacao == "subtração":
    print("Voce selecionou a subtração, o valor é:", subtracao)
elif operacao == "multiplicação":
    print("A multiplicação dos dois números é:", multiplicacao)
