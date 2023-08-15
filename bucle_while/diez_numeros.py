import random

#Escribe un programa que utilice un bucle while para imprimir los números del 1 al 10 en orden ascendente.
'''
i = 1
while( i<= 10 ): #mientras i sea menor o igual a 10. EL BUCLe se repetirá 10 veces 
    print(i)
    i= i+1 #este es para ir avanzando uno en uno. 


#Crea un programa que utilice un bucle while para calcular la suma de los números enteros del 1 al 50.
suma = 0
i = 1
while( i<= 50):
    suma +=i
    i = i+1
print(suma) '''

#Escribe un juego en el que el programa elige un número aleatorio entre 1 y 100, y el usuario debe adivinarlo. 
#El programa debe dar pistas como "Demasiado alto" o "Demasiado bajo" hasta que el usuario adivine correctamente.

def adivine_el_number():
    numero_aleatorio = random.randint(1, 100) #este random incuye los umeros 1 y el 100 cuando general el numero
    print(numero_aleatorio)

    while True: #Cuando usamos while True, estamos creando un bucle que se ejecutará continuamente porque True siempre es verdadero. Esto significa que lo que pongamos dentro del bucle se repetirá sin parar, a menos que en algún punto le digamos que se detenga.
      numero_ingresado = int(input("Ingrese el numero: "))
      if numero_aleatorio == numero_ingresado:
          print("Ganaste!!")
          break
      elif numero_ingresado > numero_aleatorio:
          print("Es demasiado grande plebe!!")
      else:
          print("Es demasiado pequeño raza!!")


adivine_el_number()
    