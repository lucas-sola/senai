import random

while True:
    numero_sorteado = random.randint(1, 14000000)

    numero_usuario = int(input("Digite um número entre 1 e 14000000: "))
    if numero_usuario == numero_sorteado:
        print(f"Parabéns! Você acertou! O número sorteado foi {numero_sorteado}.")
        break
    else:
        print(f"Tente novamente! O número sorteado foi {numero_sorteado}.")
