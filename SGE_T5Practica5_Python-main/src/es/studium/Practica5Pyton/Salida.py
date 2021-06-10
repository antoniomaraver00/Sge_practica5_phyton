# coding: utf-8
'''
Created on 5 feb. 2021

@author: Alvca
'''
#Creamos las variables que vamos a usar
import statistics
from statistics import mean, mode, variance
caracteristicas = []
caracteristica1 = []
caracteristica2 = []
caracteristica3 = []
caracteristica4 = []
caracteristica5 = []
#Preguntamos qué fichero queremos abrir
nombreFichero =input("Indique el nombre del fichero a abrir: ")
#Controlamos posibles errores
try:
    #Leemos el fichero y quitamos el \n
    with open (nombreFichero,'r') as archivo:
        lista = list(map(str.rstrip, archivo))
#indicamos que ocurrirá si hay errores
except OSError:
    print('No se puede abrir el archivo', nombreFichero)
#Si no hay errores seguimos ejecutando el siguiente código
else:
    archivo.close()
    print('Hemos hacedido al archivo', nombreFichero, 'correctamente')
    #Recorremos la lista y guardamos 2 nuevas listas
    x=0
    for lin in lista:
        if x==0: #Si es la primera línea guardamos en la lista de títulos
            #Leemos las líneas de la lista y la metemos en una nueva lista separando el " - "
            titulo = lin.split(" - ")
            caracteristicas.append(lin.split(" - "))
            x+=1
        else:#Si no es la primera línea, guardamos en característica
            #Leemos las líneas de la lista y la metemos en una nueva lista separando el " - "
            caracteristica = lin.split(" - ")
            caracteristicas.append(lin.split(" - "))
            #Guardamos cada característica  en su lista
            caracteristica1.append(int(caracteristica[0]))
            caracteristica2.append(int(caracteristica[1]))
            caracteristica3.append(int(caracteristica[2]))
            caracteristica4.append(int(caracteristica[3]))
            caracteristica5.append(int(caracteristica[4]))
            
    
    
    #Imprimimos el minimo, el maximo, la media, la moda y la varianza
    print("Valores Mínimos:")
    print(titulo[0]+": "+str(min(caracteristica1)))
    print(titulo[1]+": "+str(min(caracteristica2)))
    print(titulo[2]+": "+str(min(caracteristica3)))
    print(titulo[3]+": "+str(min(caracteristica4)))
    print(titulo[4]+": "+str(min(caracteristica5)))
    
    print("Valores Máximos:")
    print(titulo[0]+": "+str(max(caracteristica1)))
    print(titulo[1]+": "+str(max(caracteristica2)))
    print(titulo[2]+": "+str(max(caracteristica3)))
    print(titulo[3]+": "+str(max(caracteristica4)))
    print(titulo[4]+": "+str(max(caracteristica5)))
    
    print("Valores Média:")
    print(titulo[0]+": "+str(mean(caracteristica1)))
    print(titulo[1]+": "+str(mean(caracteristica2)))
    print(titulo[2]+": "+str(mean(caracteristica3)))
    print(titulo[3]+": "+str(mean(caracteristica4)))
    print(titulo[4]+": "+str(mean(caracteristica5)))
    
    print("Valores mediana:")
    print(titulo[0]+": "+str(statistics.median(caracteristica1)))
    print(titulo[1]+": "+str(statistics.median(caracteristica2)))
    print(titulo[2]+": "+str(statistics.median(caracteristica3)))
    print(titulo[3]+": "+str(statistics.median(caracteristica4)))
    print(titulo[4]+": "+str(statistics.median(caracteristica5)))
    
    print("Valores Moda:")
    print(titulo[0]+": "+str(mode(caracteristica1)))
    print(titulo[1]+": "+str(mode(caracteristica2)))
    print(titulo[2]+": "+str(mode(caracteristica3)))
    print(titulo[3]+": "+str(mode(caracteristica4)))
    print(titulo[4]+": "+str(mode(caracteristica5)))
    
    print("Valores Varianza:")
    print(titulo[0]+": "+str(variance(caracteristica1)))
    print(titulo[1]+": "+str(variance(caracteristica2)))
    print(titulo[2]+": "+str(variance(caracteristica3)))
    print(titulo[3]+": "+str(variance(caracteristica4)))
    print(titulo[4]+": "+str(variance(caracteristica5)))
