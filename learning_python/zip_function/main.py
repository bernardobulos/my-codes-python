# A função "zip()" combina múltiplos iteráveis (como listas, tuplas, sets e dicionários) em um único iterador. Isso facilita o gerenciamento de múltiplos índices. 🇧🇷
# The "zip()" function combines multiple iterables (such as lists, tuples, sets, and dictionaries) into a single iterator. This simplifies the management of multiple indexes. 🇺🇸
# La función "zip()" combina varios iterables (como listas, tuplas, conjuntos y diccionarios) en un único iterador. Esto simplifica la gestión de múltiples índices. 🇪🇸
# La fonction « zip() » combine plusieurs itérables (listes, tuples, ensembles et dictionnaires) en un seul itérateur, simplifiant ainsi la gestion de plusieurs index. 🇫🇷

lista_nomes = ["Ana", "Bia", "Clara"]
lista_idades = [30, 25, 35]
lista_trabalhos = ["lawyer", "engineer", "doctor"]

dados = zip(lista_nomes, lista_idades, lista_trabalhos)

for nome, idade, trabalho in dados:
    print(f"{nome} is a {idade}-year-old {trabalho}.")
