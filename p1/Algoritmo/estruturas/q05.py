#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os
#números IMPARES no vetor impar. Imprima os três vetores.

pessoa = ['a','b','c','d']

aux = pessoa[0]
pessoa[0] = pessoa[2]
pessoa[2] = aux

print(pessoa)