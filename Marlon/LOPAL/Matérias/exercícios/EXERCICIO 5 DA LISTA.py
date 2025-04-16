#-*- coding: UTF-8 -*-



kwh = float(input("diga a quantidade de kWh que voce utiliza"))
cons = input("Diga o tipo de instalação, I para industrias, R para residências, e C para comércios.")




if kwh <= 500 and cons == "R":
    preco = 0.40
    VF = kWh * preco
    print("Você deverá pagar:", VF)
elif kwh > 499 and kwh < 1001 and cons == "R":
    preco1 = 0.65
    VF1= kwh * preco1
    print("Você deverá pagar R$%.2f" % VF1)
elif kwh > 1000 and kwh <= 2501 and cons == "C":
     preco2 = 0.55
     VF2= kwh * preco2
     print("Você deverá pagar R$.2f" % VF2 )
elif kwh > 2500 and kwh <= 5001 and cons == "C":
     preco3 = 0.60
     VF3 = kwh * preco3
     print("Você deverá pagar: R$%.2f" % VF3)
elif kwh > 5000 and kwh < 10000:
    preco3 = 0.60
    VF3 = kwh * preco3
    print("Você deverá pagar: R$%.2f" % VF3)
elif kwh > 9999 and kwh <= 15001 and cons == "I":
    preco4 = 0.55
    VF4 = kwh * preco4
    print("Você deverá pagar: R$%.2f" % VF4)
elif kwh > 15000  and cons == "I":
    preco5 = 0.60   
    VF5 = kwh * preco5
    print("Você deverá pagar: R$%.2f" % VF5)


