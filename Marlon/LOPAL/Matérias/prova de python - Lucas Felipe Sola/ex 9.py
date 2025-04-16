#-*- coding: UTF-8 -*-

print("Olá! neste programa eu di o valor tortal da  sua compra! caso ela for maior que R$100, eu calcularei 5% de desconto!")
vq = int(input("Diga aqui a quantidade de itens que você comprou: "))
vi = int(input("Diga aqui o valor de cada item: "))

vrt = vi * vq
vt = vrt - (vrt * 5) / 100 
print(f"O valor total até o momento é de: {vrt}, e a quantidade de itens é de: {vq} agora, eu irei ver se ultrapassou os 100 reais! um segundo.")
if vrt > 100:
    print(f"Ok, o valor de desconto que você terá agora é de: {(vrt * 5) / 100}, este será o valor que você irá pagar: {vt}. Caso queira novamente, reinicie o programa!")
else:
    print(f"O valor não ultrapassou os 100 reais, então o valor é mesmo de {vi * vq}! Caso queira novamente, reinicie o programa!")
