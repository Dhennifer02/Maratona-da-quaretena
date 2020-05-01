
# Faça um programa que leia três numeros e mostre o maior e o menor entre eles

n1 = int(input("Primeiro numero:"))
n2 = int(input("Segundo numero:"))
n3 = int(input("Terceiro numero:"))

maior = n1
menor  =n1

if maior < n2:
    maior = n2

if maior < n3:
    maior = n3

if menor > n2:
    menor= n2

if menor > n3:
    menor= n3    

    print('o número maior é: ', maior)
    print('o número menor é: ', menor)



