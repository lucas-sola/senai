#-*- coding: UTF-8 -*-

valor_casa = float(input("Diga o valor da casa que você irá comprar e parcelar"))
salario = float(input("Diga o valor do seu salario"))
anos = int(input("Diga a quantidade de anos que voce ira parcelar"))
anos_em_meses = anos * 12
parcela = valor_casa / anos_em_meses

if parcela > (salario * 30) / 100:
    print("O valor da prestação deve ser menor que 30% do salario, aumente a quantidade de anos.")

else:
#elif parcela <= (salario * 30) / 100:
    print("O valor pode ser aceito, a parcela será de:",  parcela)

