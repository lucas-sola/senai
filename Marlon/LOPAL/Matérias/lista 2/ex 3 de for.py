#-*- coding: UTF-8 -*-

#codigo para calcular um valor fatorial

acum = 1
fat = int(input("Diga um valor"))
for x in range(1, fat+1):
    acum = acum * x

print("O fatorial de", fat," é: ", acum)
