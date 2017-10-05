"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

print("Calculando a media final")

n1 = float(input("Informe a nota do 1o Bimestre: "))
n2 = float(input("Informe a nota do 2o Bimestre: "))
n3 = float(input("Informe a nota do 3o Bimestre: "))
n4 = float(input("Informe a nota do 4o Bimestre: "))

media = (n1+n2+n3+n4) / 4;

print ("(%.2f + %.2f + %.2f + %.2f) = %.2f" %(n1,n2,n3,n4,media))
