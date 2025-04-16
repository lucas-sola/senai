#-*- coding: UTF-8 -*-

import random

numero1 = float(input("Diga um número e eu sortearei entre eles um aleatorio"))
numero2 = float(input("Diga um número e eu sortearei entre eles um aleatorio"))
numero3 = float(input("Diga um número e eu sortearei entre eles um aleatorio"))
numero4 = float(input("Diga um número e eu sortearei entre eles um aleatorio"))

numero_raandom = list = (numero1), (numero2), (numero3), (numero4)

print(random.choice(numero_raandom))
