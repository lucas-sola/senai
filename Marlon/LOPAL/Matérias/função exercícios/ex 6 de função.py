#-*- coding: UTF-8 -*-


v1 = int(input("diga aqui o valor do seu argumento! "))

def positivo_negativo_zero(v1):
    if v1 > 0:
        return "P"
    else:
        return"N"
    
print(positivo_negativo_zero(v1))