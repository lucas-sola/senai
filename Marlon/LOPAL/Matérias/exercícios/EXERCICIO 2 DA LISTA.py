#-*- coding: UTF-8 -*-


salario = float(input("Diga o valor do seu salario, caso ele ultrapasse 1250 reais, terá um aumento de 10%, case seja inferior, redução de 15%."))



if salario > 1250:
    salario_novo = (salario * 10) / 100
    print("Seu aumento será de:", (salario * 10) / 100, "e seu novo salario será:", salario_novo  + salario)
else:
   #if salario < 1250:
    reducao_salario = (salario * 15) / 100
    print("Sua redução será de", reducao_salario, " e seu novo salario é de:", salario - reducao_salario)
