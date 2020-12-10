     # Calcular  el promedio de  notas usando la programación Estrucutrada
     #Lectura de las notas

lista= []
resp=input("Desea introducir notas s/n: ")
while(resp=="s"):
    nota=int(input("Introduzca la nota 1 a 20: "))
    lista.append(nota) 
    resp=input("Desea introducir notas s/n: ")

n=len(lista)
if n>0:
    sum=0
    i=0
    while i<n:
        sum=sum+lista[i]
        i+=1 
    promedioNotas=sum/n
else:
    promedioNotas=0
print("El promedio de notas es:{}".format(promedioNotas)) 


        

