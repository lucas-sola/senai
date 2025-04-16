#-*- coding: UTF-8 -*-

print("Olá, meu nome é Lucas Sola e eu irei calcular o total de: dias, minutos e segundos. A soma de tudo será em segundos.")

d = int(input("diga a quantidade de dias aqui: "))
h = int(input("diga a quantidade de horas aqui: "))
m = int(input("diga a quantidade de minutos aqui: "))
s = int(input("diga a quantidade de segundos aqui: "))

horas_segundos = (h * 3600)
dias_segundos = ( d * 86400)
minutos_segundos = ( m * 60)

segundos_totais = dias_segundos + minutos_segundos + horas_segundos

print("O total disso em segundos é: ", segundos_totais)
