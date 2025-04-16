#-*- coding: UTF-8 -*-


v1 = input("diga aqui 10 caracteres minúsculos e eu drei quantas consoantes foram lidas!")
v2 = input("diga aqui 10 caracteres minúsculos e eu drei quantas consoantes foram lidas!")
v3 = input("diga aqui 10 caracteres minúsculos e eu drei quantas consoantes foram lidas!")
v4 = input("diga aqui 10 caracteres minúsculos e eu drei quantas consoantes foram lidas!")
v5 = input("diga aqui 10 caracteres minúsculos e eu drei quantas consoantes foram lidas!")
v6 = input("diga aqui 10 caracteres minúsculos e eu drei quantas consoantes foram lidas!")
v7 = input("diga aqui 10 caracteres minúsculos e eu drei quantas consoantes foram lidas!")
v8 = input("diga aqui 10 caracteres minúsculos e eu drei quantas consoantes foram lidas!")
v9 = input("diga aqui 10 caracteres minúsculos e eu drei quantas consoantes foram lidas!")
v10 = input("diga aqui 10 caracteres minúsculos e eu drei quantas consoantes foram lidas!")

mylist = (v1, v2, v3, v4, v5, v6, v7, v8, v9, v10)

for x in range(1, 11):
    if v1 or v2 or v3 or v4 or v5 or v6 or v7 or v8 or v9 or v10 == "a" or "e" or "i" or "u" or "o":
        print("vogal encontrada")
    else:
        print("consoante encontrada")

        
print(f"o número de consoantes encontradas foi de: {x}")      
        