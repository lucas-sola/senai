L = []

while True:
    n = int(input("oi, diga aqui 5 números inteiros(0 sai)"))
    if n == 0:
        break
    L.append(n)

x = 0

while x < len(L):
    print(L[x])
    x = x + 1

