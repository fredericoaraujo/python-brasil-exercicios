"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

Para calcular a área do círculo vamos utilizar a seguinte fórmula
Link: http://www.calcularaarea.com/circulo.htm

area = PI*raio**2

PI = 3.1415
"""

PI = 3.1415
print("Calcular a area do circulo")

raio = float(input("Informe o raio: "))

area = PI*raio**2

print("A area do com %.2f de raio e %.4f" %(raio, area))
