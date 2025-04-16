#-*- coding: UTF-8 -*-

print("Oi usuário, vou precisar da sua idade rapidinho! vou calcular quanto tempo falta pra você chegar nos 100 anos de idade!")

v0 = int(input("Diga aqui a sua idade: "))
if v0 < 0 or v0 > 100:
    print("Coloque uma idade válida!")
else:
    print(f"A o tempo que ira demorar até você ter 100 anos será de: {100 - v0}")
