# Escreva um programa que converta uma temperatura digitada em °C (Celsius) para °F (Fahrenheit). 🇧🇷
# Write a program that converts a temperature entered in °C (Celsius) to °F (Fahrenheit). 🇺🇸
# Escriba un programa que convierta una temperatura ingresada en °C (Celsius) a °F (Fahrenheit). 🇪🇸
# Écrivez un programme qui convertit une température saisie en °C (Celsius) en °F (Fahrenheit). 🇫🇷

celsius = float(input("Enter a temperature in °C (Celsius): "))
fahrenheit = celsius * 9 / 5 + 32
print(f"This temperature can be converted to {fahrenheit:.1f} °F (Fahrenheit).")
