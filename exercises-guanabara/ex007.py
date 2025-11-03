# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média. 🇧🇷
# Develop a program that reads a student's two grades, calculates their average, and displays it. 🇺🇸
# Desarrolla un programa que lea las dos calificaciones de un estudiante, calcule su promedio y lo muestre. 🇪🇸
# Concevez un programme qui lit les deux notes d'un élève, calcule sa moyenne et l'affiche. 🇫🇷

nota1 = float(input("Enter the student's first grade:: "))
nota2 = float(input("Enter the student's second grade:: "))
media = (nota1 + nota2) / 2
print(f"The student's average grade is {media:.1f}.")
