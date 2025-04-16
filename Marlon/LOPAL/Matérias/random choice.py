#-*- coding: UTF-8 -*- 

import random


v = int(input("Diga um valor de 1 a 10 aqui e eu direi um número aleatório"))

opcoes = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

nur = random.choice(opcoes)

while v == nur:
    print(f"O valor estava incorreto, tente novamente! {nur}")
