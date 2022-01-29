#Funcions Jordi per la practica 2

from draw3ratllaAlumnes import * #importa tot del fitxer de dibuixar el taulell
from random import randint
import sys

def crearDicJugadors(j,p): #per crear la "base de dades" (diccionari) dels juagdors
    dicJug={}
    if j not in dicJug: 
        dicJug[j]=p
    else:
        dicJug[j].append(p)
    return dicJug

def crearFitxerJugadors(dicJug): #per crear el fitxer
    try:
        f=open("jugadors.csv","w")
        f.write("Nom"+";"+"Punts"+"\n") #capçalera
        for j in dicJug:
            for p in j:
                f.write(str(j)+";"+str(j[p])+"\n") #escriu el nom del jugador i els punts
    except IOError:
        print("El fitxer NO s'ha CREAT correctament")
        sys.exit(0)
    return f

def imprimirJugadors(fitxerJug): #imprimeix els jugadors al final de la partida a partir del fitxer creat
    fitxerJug.readline()#fora capçalera
    for lin in fitxerJug:
        linia=lin.split(";")
        nomJug=linia[0].upper().strip()             #nomJug
        puntsJug=linia[1].strip()                   #puntsJug
        print(str(nomJug)+":"+str(puntsJug))
        
def jugadorGuanyador(dicJug): #aquesta funcio retorna el jugador amb més punts de tota la partida
    maxPunts = max(dicJug, key = dicJug.get)
    return maxPunts

if __name__=="__main__": #programa principal
    partida=input("Fer una partida S/N: ").upper()
    while partida=="S" and partida!="N":
        jugador=input("Escriu el teu nom de jugador: ")
        
        punts=0 #variable per anar guardant els punts de cada jugador
        
        dJugadors=crearDicJugadors(jugador,punts)
        
        
        partida=input("Fer una partida S/N: ").upper() #torna a demanar una partida
        
    fitxerJugadors=crearFitxerJugadors()
    imprimirJugadors(fitxerJugadors)
    print("El jugador amb més punts és: "+jugadorGuanyador(dJugadors))
    print("FI DEL PROGRAMA")