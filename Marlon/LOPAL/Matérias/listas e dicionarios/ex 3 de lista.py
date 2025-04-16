L = [0, 0, 0, 0, 0]
s = 0
x = 0

while x < 5:
    L[x] = float(input("Nota %d: " % x))
    s += L[x]
    x += 1

x = 0

while x < 5:
    print ("Nota %d: %6.2f" % (x, L[x]))
    x = x + 1
    
print ("Média: %5.2f" % (s / x))

