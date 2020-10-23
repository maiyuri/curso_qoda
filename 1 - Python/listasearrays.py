# -*- coding: utf-8 -*-
"""ListasEArrays.ipynb

Automatically generated by Colaboratory.



# **Listas e Arrays**

---
"""

livros = ["Data Science em 12 Semanas", "Startup Enxuta", "Desperte seu Gigante Interior"]
print(type(livros))

# SLICING/FATIAMENTO
print(livros[0])

# Método append
livros.append("Pé na Estrada")
print(livros)

# Função count() conta o número de aparições do elemento na lista
x = [1,2,3,4,5,6,7,8,9,10,10,10]
print(x.count(10))

# Função index() retorna o índice do elemento inserido
x.index(5)

# Função len() retorna o comprimento do objeto
print(len(x))

# Função max() retorna o valor máximo da lista
print(max(x))

# Função min() retorna o valor mínimo na lista
print(min(x))

# Função extend() extende a lista com novos valores adicionados
x.extend([11])
print(x)

# Função remove() retira o elemento apresentado da lista
x.remove(11)
print(x)

# Alterando um Elemento da lista
livros[3] = "Data Science Para Leigos"
print(livros)

# Removendo um elemento da lista
print(f"Antes de deletar temos: {livros}")
del livros[3]
print(f"Após deletar, temos: {livros}")

"""## **>>> Geralmente utilizamos a biblioteca numpy para lidar com arrays por conta da escassez built-in de python para tratamento de tal tipo.**"""

# Array armazena float/int em uma lista de valores
inteiros = [1,2,3,4,5]
print(inteiros)

# SLICING/FATIAMENTO
print(inteiros[0])

dir(list)

help(list)

"""## **>>> Exercícios**

---

1.   Crie uma lista vazia. Receba de um input do usuário 3 números e os adicione em sua lista. Printe por fim sua lista; (fácil)
"""

# Insira seu código aqui
lista = []
print("insira 3 numeros para adicionar na lista")
num1 = int(input('numero 1: '))
num2 = int(input('numero 2: '))
num3 = int(input('numero 3: '))

lista.append(num1)
lista.append(num2)
lista.append(num3)
print(lista)

"""2.   Com a lista dos números, ordene-os com algum método listado em dir(list); (médio)"""

# Insira seu código aqui
lista.sort()
lista

"""3.   Crie uma lista vazia. Receba do usuário, através de inputs, 3 palavras. Apresente-as em ordem alfabética inversa(de Z à A); (difícil)"""

# Insira seu código aqui
palavras = []
print("Me dê 3 palavras, e eu as ordenarei em ordem alfabética de Z à A!")
palavra1 = str(input("Palavra 1: "))
palavra2 = str(input("Palavra 2: "))
palavra3 = str(input("Palavra 3: "))

palavras.append(palavra1)
palavras.append(palavra2)
palavras.append(palavra3)

palavras.sort(reverse=True)
palavras

"""## **>>> Solução**"""

# Exercício 1
x = []
n1 = int(input("Digite um número inteiro: "))
x.append(n1)
n2 = int(input("Outro número inteiro, por favor: "))
x.append(n2)
n3 = int(input("Ok, este é o último: "))
x.append(n3)
print(x)

# Exercício 2
print(f"Os números, em ordem crescente são: {sorted(x)}")

# Exercício 3
y = []
a1 = input("Qual seu nome? ")
y.append(a1)
a2 = input("Qual sua cor favorita? ")
y.append(a2)
a3 = input("Qual sua música favorita? ")
y.append(a3)
y = sorted(y)
for elemento in reversed(y):
  print(elemento)

"""# **Obrigado!**

---
"""
