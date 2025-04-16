acum = 0 
cont = 0 

while True:
   soma = int(input("Diga aqui o valor que você deseja fazer a média: "))
   if soma < 0:
        break
   acum = acum + 1
   cont = cont + soma
print("A soma dos valores é:", cont)
print("A média dos valores é:", cont/acum)
