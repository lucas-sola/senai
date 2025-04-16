temperatura = 0 
fahrenheit = 0

def conversao(temperatura):
    temperatura = int(input("diga o valor da temperatura em celsius, digite -999 caso queira em fahrenheit"))
    if temperatura == -999:
        temperatura_f = int(input("diga aqui o valor que você quer que converta: "))
        temperatura_f = (5 / 9) * (temperatura_f - 32)
    else:
            fahrenheit = (temperatura * 1.8) + 32
            return fahrenheit 

print(conversao(temperatura))
