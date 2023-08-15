def loop():
  n= 1
  while n <= 10:
    print(n)
    n += 1

def number_pattern():
    row= 5
    for i in range(1, row+1):
        for j in range(1,i+1):
          print(j, end=" ")
        print(" ")



def Calculate():
  number = int(input("Ingrese numero:2"))
  sum = 0
  for i in range(1, number+1):
     sum += i
  print("el numero que ingreso:", number)
  print("la suma es:", sum)

def multiplication_table():
  tabla = 0
  number = int(input("ingrese el numero:"))
  for i in range (1, 10+1):
    tabla = number*i
    print(tabla)
  
def only_numbers():
  """Write a program to display only those numbers from a list that satisfy the following condition
  The number must be divisible by five
  If the number is greater than 150, then skip it and move to the next number
  If the number is greater than 500, then stop the loop 
  para resolver pensar en las condiciones de abajo hacia ariiba, considerar que el filtro menor  de 500 elimina numeros y el filtro 150 tambien, los que pasan son los que hay que dividir en 5, entonces
  hay dos filtros antes de dividir, asi no incluimos numeros que si son divisibles pero no cumple las otras .
  """
  numbers = [12, 75, 150, 180, 145, 525, 50]

  for i in numbers:
    if i > 500:
      break
    elif i > 150:
      continue
    elif i%5 == 0:
      print(i)

def print_pattern():
  row = 5
  k =5
  for i in range(0, row+1):
    for j in range(k-i, 1, -1):
      print(j, end=" ")
    print(" ")

def reverse_list():
  list1 = [10, 20, 30, 40, 50]
  largo = len(list1)
  for i in range(largo-1, 0,-1):
    lista= list1[i]
    print(lista)
    

def loop_negativo():
  num = -10
  for i in range(num,0,1):
    print(i)
   
def message_done():
  """Use else block to display a message “Done” after successful execution of for loop"""
  for i in range(5):
    print(i)
  else:
    print("Done!")

def numbers_within_range():
  """ Write a program to display all prime numbers within a range"""
  start = 25
  end = 50

  for number in range(start,end+1):
    if number > 1:
      for i in range(2, number):
         if (number%i) ==0:
           break    
      else:
          print(number)

def fibonacci():
  """ Display Fibonacci series up to 10 terms"""
  num1 = 0
  num2 = 1
  for i in range(10):
    print(num1, end=" ")
    fibo = num1 + num2
    num1 = num2
    num2 = fibo

def factorial():
  """Find the factorial of a given number"""
    
def test():
  myArray = [1,2,1,3,3,1,2,1,5,1]
  # Crear un diccionario con todas las claves posibles
  frecuencias = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

  # Contar la frecuencia de cada número en el arreglo y actualizar el diccionario
  for num in myArray:
      frecuencias[num] += 1

  # Imprimir un histograma para cada número
  for num, frecuencia in frecuencias.items():
      print(f"{num}: {'*' * frecuencia}")


if __name__ == "__main__":
  #Calculate()
  #number_pattern()
  #loop()
  #multiplication_table()
  #only_numbers()
  #print_pattern()
  #reverse_list()
  #loop_negativo()
  #message_done()
  #numbers_within_range()
  fibonacci()
