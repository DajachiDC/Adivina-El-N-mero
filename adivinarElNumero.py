import random, os
from time import sleep

print("\n==============================")
print("Juego: Adivina el Número")
print("Create By: Dajachi")
print("==============================")

input("\nENTER para jugar!!")


print("\n** MENÚ **")
print("1. Usuario de Linux")
print("2. Usuario de Windows")

print("\n## INFO ##\n\nSelecciona tu usuario correspondiente para que el programa\nfuncione correctamente.")

opcion = input("\nSeleccione una opción: ")

if opcion == "1":
    def juego():
        numeroRandom = random.randint(1,100)
        intentos = 0
        while True:
            os.system("clear")
            print("\nElije un número entre 1 y 100:")
            numero = int(input("-> "))

            if numero > 100:
                print("\nTienes que elegir un número menor a 100.")
                sleep(2)
            
            elif numero < 1:
                print("\nTienes que elegir un número mayor a 1.")
                sleep(2)
            
            elif numero > numeroRandom:
                print("\nEl número es menor.")
                intentos += 1
                sleep(2)
            
            elif numero < numeroRandom:
                print("\nEl número es mayor.")
                intentos += 1
                sleep(2)
            
            elif numero == numeroRandom:
                print(f"\n¡Felicidades! Has acertado el numero en {intentos + 1} intentos.")
                print(f"Número random: {numeroRandom} - Tu elección: {numero}")
                input("\n")
                break

    juego()


elif opcion == "2":
    def juego():
        numeroRandom = random.randint(1,100)
        intentos = 0
        while True:
            os.system("cls")
            print("\nElije un número entre 1 y 100:")
            numero = int(input("-> "))

            if numero > 100:
                print("\nTienes que elegir un número menor a 100.")
                sleep(2)
            
            elif numero < 1:
                print("\nTienes que elegir un número mayor a 1.")
                sleep(2)
            
            elif numero > numeroRandom:
                print("\nEl número es menor.")
                intentos += 1
                sleep(2)
            
            elif numero < numeroRandom:
                print("\nEl número es mayor.")
                intentos += 1
                sleep(2)
            
            elif numero == numeroRandom:
                print(f"\n¡Felicidades! Has acertado el numero en {intentos + 1} intentos.")
                print(f"Número random: {numeroRandom} - Tu elección: {numero}")
                input("\n")
                break

    juego()

else:
    print("¡Opción Incorrecta!")