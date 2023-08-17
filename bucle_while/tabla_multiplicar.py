#Solicita al usuario un número y muestra la tabla de multiplicar de ese número utilizando un bucle while.

def multilplique_su_numero():
    numero_ingresado = int(input("ingrese al numero: "))
    
    i = 1
    while(i <= 10):
        mulptiplicacion = numero_ingresado * i
        i += 1
        print(mulptiplicacion)

multilplique_su_numero()