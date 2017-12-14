import re
# VARIAVES DE LEITURA DE DADOS
JOGADOR1 = open('jogador1.txt', 'r')
JOGADOR2 = open('jogador2.txt', 'r')
RESULTADO = open('resultado.txt', 'w')
# VARIAVEIS PEÇAS JOGADOR 1 E JOGADOR 2
J1, J2, L1,L2 = {},{},[],[]
TENTATIVAJ1,TENTATIVAJ2 = [],[]



# INTRODUZIR EM CADA POSIÇÃO UMA JOGADA
for linha in JOGADOR1.readlines():
    aux = (re.split(r'[;|\n|]+', linha))
    for numero in aux:
        L1.append(numero.upper())
for linha in JOGADOR2.readlines():
    aux = (re.split(r'[;|\n|]+', linha))
    for numero in aux:
        L2.append(numero.upper())
J1[1] = L1[L1.index('1')+1:L1.index('2')-1]
J1[2] = L1[L1.index('2')+1:L1.index('3')-1]
J1[3] = L1[L1.index('3')+1:L1.index('4')-1]
J1[4] = L1[L1.index('4')+1:L1.index("#JOGADA")-1]
TENTATIVAJ1 = L1[L1.index('#JOGADA')+3:len(L1)]
J2[1] = L2[L2.index('1')+1:L2.index('2')-1]
J2[2] = L2[L2.index('2')+1:L2.index('3')-1]
J2[3] = L2[L2.index('3')+1:L2.index('4')-1]
J2[4] = L2[L2.index('4')+1:L2.index("#JOGADA")-1]
TENTATIVAJ2 = L2[L2.index('#JOGADA')+3:len(L2)]










'''for i in range(0,4):
    J1[i] = J1[i].replace(J1[i][:2],'')
    J2[i] = J2[i].replace(J2[i][:2], '')
    J1[i] = J1[i].replace('\n', '')
    J2[i] = J2[i].replace('\n', '')
J1.remove(J1[4])
J1.remove(J1[4])
J2.remove(J2[4])
J2.remove(J2[4])
print(J1)
print(J2)'''


'''
TABULEIRO={}
TABULEIRO['A'] = []
TABULEIRO['B'] = []
TABULEIRO['C'] = []
TABULEIRO['D'] = []
TABULEIRO['E'] = []
TABULEIRO['F'] = []
TABULEIRO['G'] = []
TABULEIRO['H'] = []
TABULEIRO['I'] = []
TABULEIRO['J'] = []
TABULEIRO['L'] = []
TABULEIRO['M'] = []
TABULEIRO['N'] = []
TABULEIRO['O'] = []
TABULEIRO['P'] = []
'''

'''dic = {}
    for p in texto:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p]+= 1
OCORRENCIA DE PALAVRAS 
'''

'''
matriz = []
for i in range(15):
    linhas = []
    for j in range(15):
        linhas.append(0)
    matriz.append(linhas)
#Exibir tabuleiro
numero_de_linhas = len(matriz)
numero_de_colunas = len(matriz[0])
for i in range(numero_de_linhas):
    for j in range(numero_de_colunas):
        #%6d define qual tamanho da distancia
        print("%3d" %(matriz[i][j]), end="")
    # pule uma linha
    print()

'''

