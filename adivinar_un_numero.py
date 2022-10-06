#Adivinar un número:
import random

print("------------------------------")
print("--- ADIVINAR - UN - NÚMERO ---")
print("------------------------------")

#Input
K = int(input("Intenta adivinar  mi número: "))

#Processing
N = random.randint(1,1000)
rand = 0
while  N != K:
    rand = rand + 1
    K = int(input("Adivina mi número: "))
    if K < N:
        print(" El número a adivinar es mayor")
    elif K > N:
        print("El número a adivinar es menor")
    elif K == N:
        print("¡MUY BIEN! Has acertado, el número es: " , N,"lo hiciste en:" ,rand,"intentos")