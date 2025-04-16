#-*- coding: UTF-8 -*-

cigarros_por_dia = int(input("Diga a quantidade média de cigarros fumados por dia:"))
anos = int(input("Diga a quantidade de anos que você fumou"))

anosemdias = anos * 365
cigarros = anosemdias * cigarros_por_dia
cigarrospordia = cigarros * 0.0069



print(f"A quantidade de dias que você perdeu é de:", cigarrospordia)

ellipsis("hamburgue de quejjo %.2f")