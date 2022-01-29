from http.client import OK
from unittest import case
from draw3ratllaAlumnes import draw
import sys
import random

#Funcio en la que es crea el document
def crarDocument():
    try:
        f=open("partides.csv","w")
        f.close()
    except IOError:
        print("No s'ha trobat el fitxer")
        sys.exit(0)

#Funcio en la que es modifica el document
def modificaDocument(nom,jug):
    f=open("partides.csv","w")
    llista=f.readlines()
    #for jugador in llista:
        #if nom in jugador:
            #if jug==1:
                #sumar una victoria
            #else:
                #pass
                #Sumar una derrota
        #else:
            #f.write(nom)
            #f.write("0")
            #f.write("0")
    f.close()


#Funcio en la que s'imprimeix en ordre els jugadors amb mitjana, victoria i derrota
def imprimeixFinal():
    try:
        llistaOrdenar=[]
        f=open("partides.csv","r")
        llista=f.readlines()
        for jugador in llista:
            resultats=jugador.split(";")
            #El que fem aqui es crear una llista de llistes així: llista=[[mitjana,victories,derrotes,nomJug],[...]]
            #D'aquesta manera podem ordenar els jugadors en l'ordre corresponent
            llistaOrdenar.append([resultats[1]/(resultats[1]+resultats[2]),resultats[1],resultats[2],resultats[0]])
        llistaOrdenar.sort()
        for jugadors in llistaOrdenar:
            print(jugadors[3],"\t",jugadors[3],"   ",jugadors[0],"   ",jugadors[1],"   ",jugadors[2])
        f.close()
    except IOError:
        print("No s'ha trobat el fitxer")
        sys.exit(0)

#Funcio en la que només s'imprimeixen noms
def imprimeixllistaJugadors(partides):
    try:
        f=open(partides,"r")
        Llista=f.readlines()
        f.close()
        for i in Llista:
            noms=i.split(";")
            impri=noms[0]
            print (impri)
    except IOError:
        print("No s'ha trobat el fitxer")
        sys.exit(0)    

#Funcio que demana al jugador qui comença el joc i ho retorna, 
# en cas de digui aleatori ja retorna un jugador aleatoriament
def escullJugador():
    print("Escull el jugador que comença ")
    print("1. Jugador")
    print("2. Màquina")
    print("3. Aleatori")
    jug=int(input("Opció: "))
    while jug!=1 and jug!=2 and jug!=3:
         jug=int(input("Opció: "))
    #si s'ha premut el 3 calculem aleatoriament un nombre entre 1 i 2
    if jug == 3:
        jug=random.randint(1,2)    
    return jug

#Funcio que fa canvi de les lletres(files) a numeros(0,1,2)
def canviLletra(lletra):

    if lletra.upper() == "A": 
        num=0
    elif lletra.upper() == "B":
        num=1
    elif lletra.upper() == "C":
        num=2
    return num

#Funcio que separa una posicio en dos
def separarDos(posi):
    fila=canviLletra(posi[0])
    column=int(posi[1])-1
    return fila,column

#Funcio que comprova que la posicio donada sigui correcte, ex. no D7
def comprovarPosi(posi):
    fila=posi[0].upper()
    column=int(posi[1])
    return ((fila=="A" or fila=="B" or fila=="C") and (column==1 or column==2 or column==3))

#Funcio en la que l'huma fa la jugada, es a dir, primer es comprova si ja te totes les fitxes en joc, 
# en cas de que les tingui treu una i la posa en un altre lloc vàlid o bé nomes posa una fitxa 
# en un lloc valid
def jugHuma(tauler):
    #print(tauler)
    if triple(tauler,'X'):
        tret=humatreu(tauler)
        fila,column=separarDos(tret)
        #print(fila, column)
        tauler[fila][column]=""
    #print(tauler)
    posar=humaposa(tauler)
    fila,column=separarDos(posar)
    tauler[fila][column]='X'

    return tauler

#Funcio en la que l'huma escull on posar la fitxa, es torna una posicio correcta 
# que l'huma ha escullit
def humaposa(tauler):
    comprovant=False
    while not comprovant:
        posicio=input("Posar a FilaColumna: ")
        comprovant=comprovarPosi(posicio)
        if comprovant:
            fila,column=separarDos(posicio)
            if tauler[fila][column]!="":
                comprovant=False
    return posicio

#Funcio en la que l'huma escull una fitxa per treure-la, es torna una posicio d'una 
# fitxa que l'huma vol treure
def humatreu(tauler):
    comprovant=False
    while not comprovant:
        posicio=input("Treure a FilaColumna: ")
        comprovant=comprovarPosi(posicio)
        if comprovant:
            fila,column=separarDos(posicio)
            if tauler[fila][column]!="X":
                comprovant=False
    return posicio

#Funcio que mira si ja hi ha 3 fitxes del jugador o màquina en el tauler
def triple(tauler,tirador):
    contar=0
    for files in range(3):
        for columnes in files:
            if columnes==tirador:
                contar=+1
    #ES PODRIA FER amb el metode cadena.count(element per contar), pero es per cadenes
    return contar==3

#Funcio on es comprova si algun jugador ha guanyat
def comprovaVictoria(tauler,jug):
    if jug==1:
        fitxa='X'
    else:
        fitxa='O'
    #Horitzontalment
    final=False
    contador=0
    for i in range(0,3):
        if final!=True:
            for j in range(0,3):
                if tauler[i][j]==fitxa:
                    contador=contador+1
        if contador==3:
            final=True
        contador=0
    #Verticalment
    contador=0
    if final!=True:
        for i in range(0,3):
            if final!=True:
                for j in range(0,3):
                    if tauler[j][i]==fitxa:
                        contador=contador+1
        if contador==3:
            final=True
        contador=0
    #Diagonal(adalt esquerra-abaix dreta)
    if final!=True:
        for j in range(0,3):
                    if tauler[j][j]==fitxa:
                        contador=contador+1
        if contador==3:
            final=True
    #Diagonal(abaix esquerra-adalt dreta)
    contador=0
    for i in range(0,3):
        if tauler[i][2-i]==fitxa:
            #0,2    1,1     2,0
            contador=contador+1
    if contador==3:
        final=True
    return final

#Funcio en la que es desenvolupa el joc, es torna 1 si ha guanyat el jugador, 2 la màquina
def Partida(jug,metode):
    tauler=[['','',''],['','',''],['','','']]
    fi=False
    while fi == False:
        if jug==1:
            tauler=jugHuma(tauler)
        #elif jug==2:
            #tauler=jugHuma(tauler)
            #tauler=jugMaq(tauler,metode)

        if comprovaVictoria(tauler,jug) == True:
            return jug
        #En cas de que ninú hagi guanyat, invertim 'rols' i tornem a començar
        if jug==1:
             jug=2
        else:
            jug=1
        


        
if __name__=="__main__":

    volsFer=input("Vols fer una partida? (S/N): ").upper()
    while volsFer!="S" and volsFer!="N":
        volsFer=input("Vols fer una partida? (S/N): ").upper()
    if volsFer!="N":
        crarDocument()
        print("El document està vuit")
    while volsFer=="S":
        #La primera vegada no imprimeixllistaJugadors(partides)
        nom=input("Introdueix el teu nom: ")
        metodeJoc=input("Aleatòria o Intel·ligent (A/I): ")
        while metodeJoc!="A" and metodeJoc!="I":
            metodeJoc=input("Aleatòria o Intel·ligent (A/I): ")
        iniciador=escullJugador()
        guanyador=Partida(iniciador,metodeJoc)
        if guanyador==1:
            print("Has guanyat")
        else:
            print("Has perdut")
        modificaDocument(nom,guanyador)
        volsFer=input("Vols fer una partida? (S/N): ")
        while volsFer!="S" and volsFer!="N":
            volsFer=input("Vols fer una partida? (S/N): ")
    
    if volsFer=="N": #Tot i que aqui només pot ser N
        print("Jugador","\t","Mitjana  ","Guaynat  ","Perdut")
        imprimeixFinal()


        print("Ja funciona !!!!")