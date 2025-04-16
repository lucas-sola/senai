

v1 = float(input("diga aqui o número que você quer calcular (apenas dois)"))
v2 = float(input("diga aqui o número que você quer calcular (apenas dois)"))

verif = input("diga aqui qual tipo de função matemática você quer fazer: (escreva corretamente e sem acentos!)")

if verif == "multiplicacao:":
    print(f"o valor é:{v1} * {v2} = {v1 * v2} ")
elif verif == "soma":
    print(f"o valor é:{v1} + {v2} = {v1 + v2} ")
elif verif == "subtracao":
    print(f"o valor é:{v1} - {v2} = {v1 - v2} ")
elif verif == "divisao":
    print(f"o valor é:{v1} / {v2} = {v1 / v2} ")
