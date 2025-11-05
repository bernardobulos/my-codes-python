# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m². 🇧🇷
# Write a program that reads the width and height of a wall in meters, calculates its area, and determines the amount of paint needed to paint it, knowing that each liter of paint covers an area of ​​2m². 🇺🇸
# Escribe un programa que lea el ancho y el alto de una pared en metros, calcule su área y determine la cantidad de pintura necesaria para pintarla, sabiendo que cada litro de pintura cubre un área de 2 m². 🇪🇸
# Écrivez un programme qui lit la largeur et la hauteur d'un mur en mètres, calcule sa surface et détermine la quantité de peinture nécessaire pour le peindre, sachant que chaque litre de peinture couvre une surface de 2 m². 🇫🇷

largura = float(input("Enter the wall width: "))
altura = float(input("Enter the wall height: "))
area = largura * altura
tinta = area / 2
print(f"The wall has dimensions of {largura}×{altura}, and an area of {area:.2f} m². Therefore, {tinta:.2f} liters will be needed to paint the entire wall.")
