# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Por exemplo: Digite um número: 1834; Unidade: 4; Dezena: 3; Centena: 8; Milhar: 1. 🇧🇷
# Write a program that reads a number from 0 to 9999 and shows each digit separately on the screen. For example: Enter a number: 1834; Unit: 4; Ten: 3; Hundred: 8; Thousand: 1. 🇺🇸
# Haz un programa que lea un número del 0 al 9999 y muestre en pantalla cada uno de los dígitos por separado. Por ejemplo: Ingresa un número: 1834; Unidad: 4; Decena: 3; Centena: 8; Millar: 1. 🇪🇸
# Faites un programme qui lit un nombre de 0 à 9999 et affiche à l’écran chacun des chiffres séparément. Par exemple : Entrez un nombre : 1834 ; Unité : 4 ; Dizaine : 3 ; Centaine : 8 ; Millier : 1. 🇫🇷

num = int(input("Enter a number from 0 to 9999: "))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f" — Units: {unidade}")
print(f" — Tens: {dezena}")
print(f" — Hundreds: {centena}")
print(f" — Thousands: {milhar}")
