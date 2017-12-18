import re

JOGADOR1 = open('jogador1.txt', 'r')
JOGADOR2 = open('jogador2.txt', 'r')
RESULTADO = open('resultado.txt', 'w')

J1, J2, L1,L2 = {},{},[],[]
TOTAL1, TOTAL2 = [],[]
J1CD1, J1CD2, J1CD3, J1CD4 = [],[],[],[]
J2CD1, J2CD2, J2CD3, J2CD4 = [],[],[],[]
CONTAGEM1, CONTAGEM2, listaTJ1, listaTJ2 = [],[],[],[]
NUMEROS1,NUMEROS2,LETRASJ1,LETRASJ2 = [],[],[],[]
TODOJ1, TODOJ2 = [], []
TABULEIRO = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P']
NUMERO = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
sub = 0
ACERTOS = []
global SJ1,SJ1
# INTRODUZIR EM CADA POSIÇÃO UMA JOGADA

for linha in JOGADOR1.readlines():
    aux = (re.split(r'[;|\n|]+', linha))
    for numero in aux:
        L1.append(numero.upper())
for linha in JOGADOR2.readlines():
    aux = (re.split(r'[;|\n|]+', linha))
    for numero in aux:
        L2.append(numero.upper())
        
# TRABALHANDO COM OS ARQUIVOS

J1[1] = L1[L1.index('1')+1:L1.index('2')-1]
J1[2] = L1[L1.index('2')+1:L1.index('3')-1]
J1[3] = L1[L1.index('3')+1:L1.index('4')-1]
J1[4] = L1[L1.index('4')+1:L1.index("#JOGADA")-1]
TJ1 = L1[L1.index('#JOGADA')+3:len(L1)]
J2[1] = L2[L2.index('1')+1:L2.index('2')-1]
J2[2] = L2[L2.index('2')+1:L2.index('3')-1]
J2[3] = L2[L2.index('3')+1:L2.index('4')-1]
J2[4] = L2[L2.index('4')+1:L2.index("#JOGADA")-1]
TJ2 = L2[L2.index('#JOGADA')+3:len(L2)]

for i in J1:
    for x in J1[i]:
        CONTAGEM1.append(x)
i = x = 0
for i in J2:
    for x in J2[i]:
        CONTAGEM2.append(x)

for teste in (TJ1):
    listaTJ1.append(teste[:1])
    NUMEROS1.append(teste[1:])
for teste2 in (TJ2):
    listaTJ2.append(teste2[:1])
    NUMEROS2.append(teste2[1:])
#JUNCAO1,JUNCAO2 = [],[]
JUNCAO1 = J1[1]+J1[2]+J1[3]+J1[4]
JUNCAO2 = J2[1]+J2[2]+J2[3]+J2[4]
for teste3 in (JUNCAO1):
    LETRASJ1.append(teste3[:1])
    NUMEROS1.append(teste3[1:])
NUMEROS1[20]=NUMEROS1[20][:-1:]
NUMEROS1[21]=NUMEROS1[21][:-1:]
NUMEROS1[22]=NUMEROS1[22][:-1:]
NUMEROS1[23]=NUMEROS1[23][:-1:]
NUMEROS1[29]=NUMEROS1[29][:-1:]
NUMEROS1[30]=NUMEROS1[30][:-1:]
NUMEROS1[31]=NUMEROS1[31][:-1:]
NUMEROS1[32]=NUMEROS1[32][:-1:]

for teste4 in (JUNCAO2):
    LETRASJ2.append(teste4[:1])
    NUMEROS2.append(teste4[1:])
NUMEROS2[20]=NUMEROS2[20][:-1:]
NUMEROS2[21]=NUMEROS2[21][:-1:]
NUMEROS2[22]=NUMEROS2[22][:-1:]
NUMEROS2[23]=NUMEROS2[23][:-1:]
NUMEROS2[29]=NUMEROS2[29][:-1:]
NUMEROS2[30]=NUMEROS2[30][:-1:]
NUMEROS2[31]=NUMEROS2[31][:-1:]
NUMEROS2[32]=NUMEROS2[32][:-1:]
a = CONTAGEM1
b = CONTAGEM2

###################################################################################################################
#Separando posição
           
for i in a[:2]:
    kkk = i[:1:]
    indice = i[1::]
    if len(i)==4:
        indice = indice[:-1:]
    else:
        indice = indice[0]
    if i[-1] == 'H':
        for cont in range(0,4):
            proximo = kkk+(str(int(indice)))
            J1CD1.append(proximo)
            indice = int(indice) + 1
    elif i[-1] == 'V':
        CONT = 0
        while (TABULEIRO[CONT]!=kkk) == True:
            CONT += 1
        for lp in range(0,4):
            proximo =  TABULEIRO[CONT+lp]+(str(int(indice)))
            J1CD1.append(proximo) 
for i in a[2:-9]:
    kkk = i[:1:]
    indice = i[1::]
    if len(i)==4:
        indice = indice[:-1:]
    else:
        indice = indice[0]
    if i[-1] == 'H':
        for cont in range(0,5):
            proximo = kkk+(str(int(indice)))
            J1CD2.append(proximo)
            indice = int(indice) + 1
    elif i[-1] == 'V':
        CONT = 0
        while (TABULEIRO[CONT]!=kkk) == True:
            CONT += 1
        for lz in range(0,5):
            proximo =  TABULEIRO[CONT+lz]+(str(int(indice)))
            J1CD2.append(proximo)
J1CD3 = J1[3]
for i in a[9::]:
    kkk = i[:1:]
    indice = i[1::]
    if len(i)==4:
        indice = indice[:-1:]
    else:
        indice = indice[0]
    if i[-1] == 'H':
        for cont in range(0,2):
            proximo = kkk+(str(int(indice)))
            J1CD4.append(proximo)
            indice = int(indice) + 1
    elif i[-1] == 'V':
        CONT = 0
        while (TABULEIRO[CONT]!=kkk) == True:
            CONT += 1
        for lq in range(0,2):
            proximo =  TABULEIRO[CONT+lq]+(str(int(indice)))
            J1CD4.append(proximo)
            
     
###################################################################################################################
for i in b[:2]:
    kkk = i[:1:]
    indice = i[1::]
    if len(i)==4:
        indice = indice[:-1:]
    else:
        indice = indice[0]
    if i[-1] == 'H':
        for cont in range(0,4):
            proximo = kkk+(str(int(indice)))
            J2CD1.append(proximo)
            indice = int(indice) + 1
    elif i[-1] == 'V':
        CONT = 0
        while (TABULEIRO[CONT]!=kkk) == True:
            CONT += 1
        for lp in rbnge(0,4):
            proximo =  TABULEIRO[CONT+lp]+(str(int(indice)))
            J2CD1.append(proximo) 
for i in b[2:-9]:
    kkk = i[:1:]
    indice = i[1::]
    if len(i)==4:
        indice = indice[:-1:]
    else:
        indice = indice[0]
    if i[-1] == 'H':
        for cont in range(0,5):
            proximo = kkk+(str(int(indice)))
            J2CD2.append(proximo)
            indice = int(indice) + 1
    elif i[-1] == 'V':
        CONT = 0
        while (TABULEIRO[CONT]!=kkk) == True:
            CONT += 1
        for lz in range(0,5):
            proximo =  TABULEIRO[CONT+lz]+(str(int(indice)))
            J2CD2.append(proximo)
J2CD3 = J1[3]
for i in b[9::]:
    kkk = i[:1:]
    indice = i[1::]
    if len(i)==4:
        indice = indice[:-1:]
    else:
        indice = indice[0]
    if i[-1] == 'H':
        for cont in range(0,2):
            proximo = kkk+(str(int(indice)))
            J2CD4.append(proximo)
            indice = int(indice) + 1
    elif i[-1] == 'V':
        CONT = 0
        while (TABULEIRO[CONT]!=kkk) == True:
            CONT += 1
        for lq in range(0,2):
            proximo =  TABULEIRO[CONT+lq]+(str(int(indice)))
            J2CD4.append(proximo)
TODOJ1 = J1CD1 + J1CD2 + J1CD3 + J1CD4 
TODOJ2 = J2CD1 + J2CD2 + J2CD3 + J2CD4 
    
########################################################################################################################################################
def main():
    # Primeiro ERRO VALIDAÇÃO
    if len(J1[1]) != 2 or len(J1[2]) != 2 or len(J1[3]) != 5 or len(J1[4]) != 4 or len(TJ1) != 20:
        #print('RESULTADO.write J1 ERROR_NR_PARTS_VALIDATION')
        RESULTADO.write("J1 ERROR_NR_PARTS_VALIDATION")
        return
    elif len(J2[1]) != 2 or len(J2[2]) != 2 or len(J2[3]) != 5 or len(J2[4]) != 4 or len(TJ2) != 20:
        #print('RESULTADO.write J2 ERROR_NR_PARTS_VALIDATION ')
        RESULTADO.write("J2 ERROR_NR_PARTS_VALIDATION")
        return

  
     #Segundo ERRO OVERWRITE VALIDAÇÃO
    for conta15 in range(0,len(TODOJ1)):
        if TODOJ1.count(TODOJ1[conta15]) > 1:
            #print('RESULTADO.write J1 ERROR_OVERWRITE_PIECES_VALIDATION')
            RESULTADO.write('J1 ERROR_OVERWRITE_PIECES_VALIDATION')
            return
        
    for conta16 in range(0,len(TODOJ2)):
        if TODOJ2.count(TODOJ2[conta16]) > 1:
            #print('RESULTADO.write J2 ERROR_OVERWRITE_PIECES_VALIDATION')
            RESULTADO.write('J2 ERROR_OVERWRITE_PIECES_VALIDATION')
            return

    # Erro ERROR_POSITION_NONEXISTENT_VALIDATION
    for letra1 in range (0,len(LETRASJ1)):
        erro = (LETRASJ1[letra1]) in TABULEIRO
        if  erro == False:
            print('J1 LETRAS')
            RESULTADO.write('J1 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return
    for NUM1 in range (0,len(NUMEROS1)):
        erro = (NUMEROS1[NUM1]) in NUMERO
        if erro == False:
            print('J1 NUMEROS')
            RESULTADO.write('J1 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return
    for T1 in range (0,len(listaTJ1)):
        erro = (listaTJ1[T1]) in TABULEIRO
        if erro == False:
            print('J1 T1 LETRAS')
            RESULTADO.write('J1 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return
        
    for letra2 in range (0,len(LETRASJ2)):
        erro = (LETRASJ2[letra2]) in TABULEIRO
        if  erro == False:
            print('J2 LETRAS')
            RESULTADO.write('J2 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return
    for NUM2 in range (0,len(NUMEROS2)):
        erro = (NUMEROS2[NUM2]) in NUMERO
        if  erro == False:
            print('J2 NUMEROS')
            RESULTADO.write('J2 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return
    for T2 in range (0,len(listaTJ2)):
        erro = (listaTJ2[T2]) in TABULEIRO
        if erro == False:
            print('J2 T2 LETRAS')
            RESULTADO.write('J2 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return
            return 
    ## JOGADOR 1 ---  

    # JOGADOR 1 -- encouraçados():
    PE1 = 0
    AAPE1 = AAPS1 = AAPC1 = AAPE1 = AAPP1 = 0
    AAPE2 = AAPS2 = AAPC2 = AAPE2 = AAPP2 = 0

    for indicePE1 in range(0,len(J1CD1)):
        psub = J1CD1[indicePE1] in TJ1
        if psub == True:
            PE1 = PE1 + 3
            AAPE1 = 1 + AAPE1
     #print('PE1',PE1)

    
    #JOGADOR 1 -- portaaviões():
    PP1 = 0
    for indicePP1 in range(0,len(J1CD2)):
        psub = J1CD2[indicePP1] in TJ1
        if psub == True:
            PP1 = PP1 + 3
            AAPP1 = 1 + AAPP1 
            ACERTOS.append(J1CD2[indicePP1])
    #print('PP1',PP1)

    # jOGADOR 1 -- submarino
    PS1 = 0
    for indicePS1 in range(0,len(J1CD3)):
        psub = J1CD3[indicePS1] in TJ1
        if psub == True:
            PS1 = PS1 + 5
            AAPS1 = AAPS1 + 1
    #print('PS1',PS1)
        
    # JOGADOR 1 -- cruzadores():
    PC1 = 0
    for indicePC1 in range(0,len(J1CD4)):
        psub = J1CD4[indicePC1] in TJ1
        if psub == True:
            PC1 = PC1 + 3
            AAPC1 = AAPC1 + 1
                
## JOGADOR 2 --- 
    # JOGADOR 2 -- encouraçados():
    PE2 = 0
    for indicePE2 in range(0,len(J2CD1)):
        psub = J2CD1[indicePE2] in TJ2
        if psub == True:
            PE2 = PE2 + 3
            AAPE2 = AAPE2 + 1
    #print('PE2',PE2)

    
    #JOGADOR 2 -- portaaviões():
    PP2 = 0
    for indicePP2 in range(0,len(J2CD2)):
        psub = J2CD2[indicePP2] in TJ2
        if psub == True:
            PP2 = PP2 + 3
            AAPP2 = AAPP2 + 1
    #print('PP2',PP2)

    # jOGADOR 1 -- submarino
    PS2 = 0
    for indicePS2 in range(0,len(J2CD3)):
        psub = J2CD3[indicePS2] in TJ2
        if psub == True:
            PS2 = PS2 + 5
            AAPS2 = AAPS2 + 1 
    #print('PS2',PS2)
        
    # JOGADOR 1 -- cruzadores():
    PC2 = 0
    for indicePC2 in range(0,len(J2CD4)):
        psub = J2CD4[indicePC2] in TJ2
        if psub == True:
            PC2 = PC2 + 3
            AAPC2 +=  AAPC2 + 1

    # SOMATORIO JOGADOR 1
    SJ2 = PS2 + PE2 + PP2 + PC2
    SJ1 = PS1 + PE1 + PP1 + PC1
    TOT1 = AAPE1 + AAPS1 + AAPC1 + AAPP1
    TOT2 = AAPE2 + AAPS2 + AAPC2 + AAPP2
    N_ACERTADO1= len(a) - TOT1
    N_ACERTADO2= len(b) - TOT2
    #SAIDA SE TUDO CERTO

    #EMPATE
    if SJ2 == SJ1:
        RESULTADO.write('J1 {}AA {}AE {}PT \nJ2 {}AA {}AE {}PT'.format(str(TOT1),str(N_ACERTADO1),str(SJ1),str(TOT2),str(N_ACERTADO2),str(SJ2)))
        return
    # JOGADOR 1 - GANHOU
    if SJ1 > SJ2:
        RESULTADO.write('J1 {}AA {}AE {}PT'.format(str(TOT1),str(N_ACERTADO1),str(SJ1)))
        return
    # JOGADOR 2 - GANHOU    
    if SJ2 > SJ1:
        RESULTADO.write('J2 {}AA {}AE {}PT'.format(str(TOT2),str(N_ACERTADO2),str(SJ2)))
        return

#Inicia a Função
main()
RESULTADO.close()
JOGADOR1.close()
JOGADOR2.close()
exit()








