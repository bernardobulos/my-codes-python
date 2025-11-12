# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada. 🇧🇷
# The same teacher from the previous challenge wants to randomly determine the order in which students will present their work. Write a program that reads the names of the four students and displays the randomly selected order. 🇺🇸
# El mismo profesor del reto anterior quiere determinar aleatoriamente el orden en que los alumnos presentarán sus trabajos. Escribe un programa que lea los nombres de los cuatro alumnos y muestre el orden seleccionado aleatoriamente. 🇪🇸
# Le même professeur que lors du défi précédent souhaite déterminer aléatoirement l'ordre de présentation des travaux des élèves. Écrivez un programme qui lit les noms des quatre élèves et affiche l'ordre tiré au sort. 🇫🇷

from random import shuffle

nome1 = str(input("Enter the name of the 1st student: "))
nome2 = str(input("Enter the name of the 2nd student: "))
nome3 = str(input("Enter the name of the 3rd student: "))
nome4 = str(input("Enter the name of the 4th student: "))

lista_nomes = [nome1, nome2, nome3, nome4]

shuffle(lista_nomes)

print(f"The order of presentation of works will be {lista_nomes}.")
