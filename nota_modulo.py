'''
El calculo del promedio de notas utilizando la programación modular
'''
def promedioLista(l:list)->float:
    n=len(l)
    if n>0:
        sum=0
        i=0
        while i<n:
            sum=sum+lista[i]
            i+=1 
        return(sum/n)
    else:
        return(0)






lista= []
resp=input("Desea introducir notas s/n: ")
while(resp=="s"):
    nota=int(input("Introduzca la nota 1 a 20: "))
    lista.append(nota) 
    resp=input("Desea introducir notas s/n: ")

print("El promedio de notas es:{}".format(promedioLista(lista))) 

