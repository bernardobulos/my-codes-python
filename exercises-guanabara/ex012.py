# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 🇧🇷
# Write an algorithm that reads the price of a product and displays its new price, with a 5% discount. 🇺🇸
# Escribe un algoritmo que lea el precio de un producto y muestre su nuevo precio con un descuento del 5%. 🇪🇸
# Écrivez un algorithme qui lit le prix d'un produit et affiche son nouveau prix, avec une réduction de 5 %. 🇫🇷

preco = float(input("Enter the product price: R$ "))
desconto = preco * 0.05
print(f"The new price of this product, with a 5% discount, is R$ {preco - desconto:.2f}.")
