#-*-coding:UTF-8-*-
print("Insira dois números e eu somarei os números ímpares entre eles, os incluindo!")
a=int(input("Digite o primeiro número: "))
b=int(input("Digite o segundo número: "))

if a>=b:
    a1=a
    a=b
    b=a1
elif a<0 or b<0:
    print("Você inseriu números inválidos!")
else:
    def calculo(x):
        vi=0
        soma=0
        for x in range(a, b+1):
            vi=x%2
            if vi!=0:
                soma=soma+x
        print(f"O valor da soma dos números ímpares entre {a}(A) e {b}(B) é de: {soma}!")
calculo(1)
    

