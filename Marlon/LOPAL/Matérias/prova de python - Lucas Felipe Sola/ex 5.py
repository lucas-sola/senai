#-*- coding: UTF-8 -*-
print("Olá usuário! aqui eu direi a você a soma dos números ímpares do número de sua escolha!")
cont = 0

n = int(input("Diga aqui um valor"))
for x in range (1, n):
      if x % 2 != 0:
            cont = cont + x
            print(f"Os valores ímpares são: {x}, já as somas são: {cont}")
