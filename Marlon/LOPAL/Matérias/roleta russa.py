import os
import random

v1 = int(input("Olá, diga aqui um número de 1 a 6, caso ele seja igual ao que o programa roletar, System32 será excluído."))
v2 = random.randint(1,6)

print(v2)

if v1 == v2:
    print("acabou para voce.")
    