#-*-coding: UTF-8 -*-

nome1 = int(input("Diga sua idade e eu direi se pode ou nao tirar a reservista: "))

if nome1 < 15:
    print("você não pode tirar a reservista ")
else:
         if nome1 >= 15 and nome1 < 18:
             print("Você pode tirar a reservista ")
             else:
                 if nome1 >= 18 and nome1 < 60:
            print("Você deve tirar a reservista ")
             else:
                if nome1 >= 60:
                    print("Você não é mais obrigado a votar ")
    
