L = []

while True:
    n = int(input("Digite um número (0 sai): "))
    if n == 0:
        break
    L.append(n)

L.reverse()
print(L)

