# coding: utf-8
'''
Created on 5 feb. 2021

@author: Alvca
'''
from random import randint

nombreFichero =input("Indique el nombre del fichero: ")
print("Los datos se guardaran el el fichero " +nombreFichero)

nombreCaracteristica1 =input("Indique el nombre de la primera característica: ")
rangoValor1=int(input("Indique el máximo de la primera característica: "))
print("La primera característica es " +nombreCaracteristica1 + " y tiene un rango del 0 al "+str(rangoValor1))
  
nombreCaracteristica2 =input("Indique el nombre de la segunda característica: ")
rangoValor2=int(input("Indique el máximo de la segunda característica: "))
print("La segúnda característica es " +nombreCaracteristica2 + " y tiene un rango del 0 al "+str(rangoValor2))
  
nombreCaracteristica3 =input("Indique el nombre de la tercera característica: ")
rangoValor3=int(input("Indique el máximo de la tercera característica: "))
print("La tercera característica es " +nombreCaracteristica3 + " y tiene un rango del 0 al "+str(rangoValor3))
  
nombreCaracteristica4 =input("Indique el nombre de la cuarta característica: ")
rangoValor4=int(input("Indique el máximo de la cuarta característica: "))
print("La cuarta característica es " +nombreCaracteristica4 + " y tiene un rango del 0 al "+str(rangoValor4))
  
nombreCaracteristica5 =input("Indique el nombre de la quinta característica: ")
rangoValor5=int(input("Indique el máximo de la quinta característica: "))
print("La quinta característica es " +nombreCaracteristica5 + " y tiene un rango del 0 al "+str(rangoValor5))

#Asignacion de variables sin teclado, para pruebas rápidas
# nombreCaracteristica1 = "Goles"
# rangoValor1 = int(20)
# nombreCaracteristica2 = "Pérdidas de balón en área propia"
# rangoValor2 = int(50)
# nombreCaracteristica3 = "Pérdidas de balón en área contraria"
# rangoValor3 = int(50)
# nombreCaracteristica4 = "Pases efectivos"
# rangoValor4 = int(50)
# nombreCaracteristica5 = "Pases fallados"
# rangoValor5 = int(50)

fichero = open (nombreFichero,'a') #"w" Borramos lo anterior y escribimos archivo nuevo, "a" añadimos al archivo existente, "r" abrimos en modo solo lectura.
fichero.write(nombreCaracteristica1+" - "+nombreCaracteristica2+" - "+nombreCaracteristica3+" - "+nombreCaracteristica4+" - "+nombreCaracteristica5+"\n")
registros = 0
#Realizamos la acción hasta tener 1000 Registros
while registros < 1000:
    #Generamos los valores aleatorios para cada característica.
    carasteristica1RDN= randint(0,rangoValor1)
    carasteristica2RDN= randint(0,rangoValor2)
    carasteristica3RDN= randint(0,rangoValor3)
    carasteristica4RDN= randint(0,rangoValor4)
    carasteristica5RDN= randint(0,rangoValor5)
    #Guardamos los datos en una línea
    line= ""+str(carasteristica1RDN)+" - "+str(carasteristica2RDN)+" - "+str(carasteristica3RDN)+" - "+str(carasteristica4RDN)+" - "+str(carasteristica5RDN)+"\n"
    #archivo-salida.py
   
    fichero.write(line) #Escribimos la línea
    registros+=1
fichero.close() #cerramos el archivo
