print("Olá usuário, neste programa, eu irei calcular a média de 5 números que você quiser!")

x = 1
soma = 0
while x <= 5:
    n = int(input("Digite o número aqui:"))
    soma = soma + n
    x = x + 1
print (f"A média final é igual a: {soma / 5}")
