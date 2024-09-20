import random
num_secreto= random.randint(1,10)
int= 0
error= 0


print ("Bienveido, adivina el numero secreto")

while num_secreto not numero: # type: ignore
 
 numero= int(input("Ingresa el numero"))

 if num_secreto== numero:
    int= int+1 
    error= error
    print("Felicidades adivinaste el numero secreto")
    print ("Lo hiciste en", int, "intentos y", error,)
    break
 
 if num_secreto < numero:
    print(" El numero secreto es menor")
    int= int+1
    error= error+1

 if num_secreto > numero:
    print("El numero secreto es mayor")
    int= int+1
    error= error+1
    

   


 


