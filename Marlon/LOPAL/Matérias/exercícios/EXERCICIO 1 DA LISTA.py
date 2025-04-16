#-*- coding: UTF-8 -*-

velocidade = int(input("Diga a velocidade que você estava no carro"))

if velocidade > 80:
    multa = ((velocidade - 80)  * 5)
    print("Voce foi multado, cada km acima de 80 será cobrado 5 reais, ou seja, será cobrado:", multa)
else:
    print("parabéns pela boa conduta!")
