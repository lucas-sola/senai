#-*- coding: UTF-8 -*-

v1 = float(input("Diga três numeros e eu direi qual e maior e se é positivo ou negativo"))
v2 = float(input("Diga três numeros e eu direi qual e maior e se é positivo ou negativo"))
v3 = float(input("Diga três numeros e eu direi qual e maior e se é positivo ou negativo"))

if v1 < 0:
    print("bom, o primeiro valor é negativo..")
if v2 < 0:
    print("bom, o segundo valor é negativo.")
if v3 < 0:
    print("bom,  o terceiro é negativo")

if v1 > 0:
    print("bom, o primeiro valor é positivo.")
if v2 > 0:
    print("bom, o segundo valor é positivo.")
if v3> 0:
    print("bom, o terceiro valor é positivo.")

if v1 > v2 and v1 > v3:
          print(v1, "é o maior valor")
if v2 > v1 and v2 > v3:
          print(v2, "é o maior valor")
if v3 > v1 and v3 > v2:
          print(v3, "é o maior valor")


