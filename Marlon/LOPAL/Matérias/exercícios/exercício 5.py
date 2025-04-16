#-*- coding: UTF-8 -*-

#calcular o desconto de uma mercadoria

VP = float(input("Diga o valor do produto original"))
VD = float(input("Diga o valor atual de desconto"))

VF = ((VP * VD) / 100)

print("A porcentagem de desconto é:", VF)

VT = VP - VF

print("O valor ja descontado será de:", VT)





