#-*- coding: UTF-8 -*-


kmp = float(input("Diga a quantidade de kilômetros que o seu carro percorreu durante os dias:"))
dag = int(input("Diga a quantidade de dias que você alugou o carro"))

vapg = kmp * 0.15
vpd = dag * 60

valor_total = vapg + vpd

print("O valor que você terá que pagar durante os dias e kms rodados são:", valor_total) 


