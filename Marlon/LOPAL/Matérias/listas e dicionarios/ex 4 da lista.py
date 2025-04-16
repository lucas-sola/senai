#-*- coding: UTF-8 -*-
L = []
O = []
ca = 0
while ca < 10:
    v = input("diga aqui um caractere e eu direi se é uma vogal ou não! digite 0 para sair")
    if v == "0":
        break
    ca = ca + 1
    if v == "a" or v == 'e' or v == 'i' or v == 'u' or v == 'o':
        O.append(v)
        print("vogal!")
    else:
        L.append(v)
        print("consoante")


print("Os caracteres digitados até o momento foram esses.")
print("As vogais foram:")
print(len(O))
print("E as consoantes foram: ")
print(len(L))




        
