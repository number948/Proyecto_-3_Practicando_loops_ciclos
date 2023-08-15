myArray = [1,2,2,4,5,6,7,8,8,8]

concurrencia = 1
longest = 0
number = 0
posicion = myArray[0]

for i in range(1,  len(myArray)):
    if myArray[i] == myArray[i-1]:
        concurrencia +=1
    else:
        if concurrencia > longest:
            longest= concurrencia
            number = posicion
        concurrencia = 1
        posicion = myArray[i]
  
if concurrencia> longest:
    longest =  concurrencia
    number = posicion

print(f"Longest: {longest} \nNumber: {number}")

