# -*- coding: utf-8 -*-
x = float(input("Digite um numero: "))
y = float(input("Digite outro numero: "))
calc = int(input("Digite 1 pra soma, 2 pra menos, 3 pra multiplicação, 4 pra divisao: "))

if calc == 1:
    print(x+y)
elif calc == 2:
    print(x-y)
elif calc == 3:
    print(x*y)
elif calc == 4:
    print(x/y)
else:
    print("numero invalido")