#-*- coding: UTF-8 -*-
    
print("olá, eu irei calcular a soma do seu salário, meu nome é Lucas Sola.")

salario = float(input("Diga seu salário líquido aqui: "))
porcentagem = float(input
                     ("Diga a porcentagem que vai aumentar aqui: "))

salario_queijo = ((salario * porcentagem) / 100)
salario_final = salario + salario_queijo




print("o seu salario final é: ", salario_final)
print("seu aumento será ", salario_queijo)

