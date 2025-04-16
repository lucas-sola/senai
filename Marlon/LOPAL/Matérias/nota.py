v1 = int(input("Diga sua nota aqui e eu direi sua média(0-10: "))

v2 = int(input("Diga sua nota aqui e eu direi sua média (0-10): "))

v3 = int(input("Diga sua nota aqui e eu direi sua média (0-10): "))

v4 = int(input("Diga sua nota aqui e eu direi sua média (0-10): "))

v5 = int(input("Diga sua nota aqui e eu direi sua média (0-10): "))

if v1 > 10:
    print("Digite um número de 0 a 10 por favor! ")
if v2 > 10:
    print("Digite um número de 0 a 10 por favor! ")
if v3 > 10:
    print("Digite um número de 0 a 10 por favor! ")
if v4 > 10:
    print("Digite um número de 0 a 10 por favor! ")
if v5 > 10:
    print("Digite um número de 0 a 10 por favor! ")


v6 = ((v1 + v2 + v3 + v4 + v4) /5)


if v6 < 0 or v6 > 10:
    print:("Sua média é invalida, coloque outros valores. ")
else:
    print(" Sua média é:", v6)

    
