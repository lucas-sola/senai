#-*- coding UTF-8 -*-

raio = float(input("Diga aqui o valor do raio de um cilindro para eu calcular o valor do volume dele! "))
altura = float(input("Diga aqui o valor da altura de um cilindro para eu calcular o valor do volume dele! "))

def volume(raio, altura):
    resultado = 3.14 * (raio * raio) * altura
    print(f"resultado %.2f" % resultado)

volume(raio, altura)
