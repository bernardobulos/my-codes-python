# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua posição inteira. Exemplo: "Digite um número: '6.127'" Saída: "O número 6.127 tem a parte inteira 6". 🇧🇷
# Write a program that reads any real number from the keyboard and displays its integer part on the screen. Example: "Enter a number: '6.127'" Output: "The number 6.127 has an integer part of 6". 🇺🇸
# Escribe un programa que lea cualquier número real desde el teclado y muestre su parte entera en la pantalla. Ejemplo: "Introduce un número: '6.127'" Salida: "El número 6.127 tiene una parte entera de 6". 🇪🇸
# Écrivez un programme qui lit un nombre réel saisi au clavier et affiche sa partie entière à l'écran. Exemple : « Entrez un nombre : '6,127' » Sortie : « La partie entière du nombre 6,127 est 6. » 🇫🇷

from math import trunc

num = float(input("Enter a value: "))
p_int = trunc(num)
print(f"The number {num} has the integer part {p_int}.")
