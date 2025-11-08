# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 🇧🇷
# Write a program that reads any angle and displays the sine, cosine, and tangent values ​​of that angle on the screen. 🇺🇸
# Escribe un programa que lea cualquier ángulo y muestre en pantalla los valores del seno, coseno y tangente de ese ángulo. 🇪🇸
# Écrivez un programme qui lit un angle quelconque et affiche à l'écran les valeurs du sinus, du cosinus et de la tangente de cet angle. 🇫🇷

from math import radians, sin, cos, tan

angulo = float(input("Enter any angle: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f" — The sine of {angulo}° is {seno:.2f}.")
print(f" — The cosine of {angulo}° is {cosseno:.2f}.")
print(f" — The tangent of {angulo}° is {tangente:.2f}.")
