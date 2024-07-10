

########################## numeros aleatorios sem repeticoes de números ########################################   
import random

numerosEm = []
estrelasEm = []
semanas = 0
somaAcertos = 0
milhao = ""

print("*********************************************")
print("               EURO MILHÕES                  ")
print("*********************************************")

print("Faça sua aposta com 5 números de 1-50:")
apostaNr = []
apostaNr.append(int(input("Introduza 1 número: ")))
apostaNr.append(int(input("Introduza 2 número: ")))
apostaNr.append(int(input("Introduza 3 número: ")))
apostaNr.append(int(input("Introduza 4 número: ")))
apostaNr.append(int(input("Introduza 5 número: ")))

print("Faça sua aposta com 2 estrelas de 1-12:")
apostaEs = []
apostaEs.append(int(input("Introduza 1 número: ")))
apostaEs.append(int(input("Introduza 2 número: ")))

apostaNr.sort()
apostaEs.sort()

while semanas < 100:
    while len(numerosEm) < 5:
        numero = random.randrange(1,51)
        while numero in numerosEm:
            numero = random.randrange(1,51)
        numerosEm.append(numero)
        
    while len(estrelasEm) < 2:
        estrela = random.randrange(1,13)
        while estrela in estrelasEm:
            estrela = random.randrange(1,13)
        estrelasEm.append(estrela)

    acertoNr = 0
    if (apostaNr[0] == numerosEm[0] or  apostaNr[0]==numerosEm[1] or apostaNr[0]==numerosEm[2]
        or apostaNr[0]==numerosEm[3]  or apostaNr[0]== numerosEm[4]):
        acertoNr +=1
        
    if (apostaNr[1] == numerosEm[0] or  apostaNr[1]==numerosEm[1] or apostaNr[1]==numerosEm[2]
        or apostaNr[1]==numerosEm[3]  or apostaNr[1]== numerosEm[4]):
        acertoNr +=1

    if (apostaNr[2] == numerosEm[0] or  apostaNr[2]==numerosEm[1] or apostaNr[2]==numerosEm[2]
        or apostaNr[2]==numerosEm[3]  or apostaNr[2]== numerosEm[4]):
        acertoNr +=1

    if (apostaNr[3] == numerosEm[0] or  apostaNr[3]==numerosEm[1] or apostaNr[3]==numerosEm[2]
        or apostaNr[3]==numerosEm[3]  or apostaNr[3]== numerosEm[4]):
        acertoNr +=1

    if (apostaNr[4] == numerosEm[0] or  apostaNr[4]==numerosEm[1] or apostaNr[4]==numerosEm[2]
        or apostaNr[4]==numerosEm[3]  or apostaNr[4]== numerosEm[4]):
        acertoNr +=1

    acertoEs = 0
    if (apostaEs[0] == estrelasEm[0] or  apostaEs[0]==estrelasEm[1]):
        acertoEs +=1
        
    if (apostaEs[1] == estrelasEm[0] or  apostaEs[1]==estrelasEm[1]):
        acertoEs +=1
    
    if acertoEs > 0 or acertoNr > 0:
        somaAcertos += 1

    if acertoNr == 5 and acertoEs == 2:
        milhao = "Ficou milionário(a)!"

    numerosEm.sort()
    estrelasEm.sort() 
    print()
    print(f"{semanas + 1}ª semana")
    print("Números aposta",apostaNr)
    print("Números sorteados ",numerosEm," Acertou ", acertoNr, " números!")
    print()
    print("Números estrela",apostaEs)
    print("Estrelas sorteadas ", estrelasEm," Acertou ", acertoEs," estrelas!")
    print()
    
    numerosEm.clear()
    estrelasEm.clear()
    semanas +=1
print(milhao)
print("Total de semanas com pelo menos 1 acertoNr ",somaAcertos)



