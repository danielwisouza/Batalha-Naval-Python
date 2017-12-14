import glob
import os
import shutil

dirp, dirt, dira = os.path.dirname(__file__), 'temp', 'algoritmo'
JOGADOR1, JOGADOR2, RESULTADO = 'jogador1.txt', 'jogador2.txt', 'resultado.txt'
ALGORITMO = glob.glob(os.path.join(dirp, dira, '*.py'))[0].split(os.sep)[-1]

def removeAllFiles(dir):
    filelist = glob.glob(os.path.join(dir,'*.*'))
    for f in filelist:
        os.remove(f)

def compareResults(pResult, pExpected):
    result = None
    expected = open(pExpected)
    try:
        result = open(pResult)
    except IOError:
        return 'Resultado: Arquivo com o resultado processado nao encontrado'
    linesr, linese = result.read().split('\n'), expected.read().split('\n')
    
    if len(linesr) == len(linese):
        for indexLine in range(0,len(linese)):
            if linesr[indexLine].strip() != linese[indexLine].strip():
                return 'Resultado: Saidas divergentes\nEsperado: {0}\nProcessado: {1}'.format(linese[indexLine].strip(), linesr[indexLine].strip())			
        return 'Processado com sucesso'
    else:
        return 'Resultado: Numero de linhas do arquivo gerado incorretas\nEsperado: {0}\nProcessado: {1}'.format(len(linese), len(linesr))

for dirct in glob.glob('ct*'):
    removeAllFiles(os.path.join(dirp, dirt))
    shutil.copy(os.path.join(dirp, dira, ALGORITMO), os.path.join(dirp, dirt, ALGORITMO))
    shutil.copy(os.path.join(dirp, dirct, JOGADOR1), os.path.join(dirp, dirt, JOGADOR1))
    shutil.copy(os.path.join(dirp, dirct, JOGADOR2), os.path.join(dirp, dirt, JOGADOR2))
    os.chdir(os.path.join(dirp, dirt))
    cmdresult = os.system('python {0}'.format(ALGORITMO))
    os.chdir('..')
    print('-----------------------------------------------------------')
    print('Caso de Teste - {0}'.format(dirct.upper()))
    print(compareResults(os.path.join(dirp, dirt, RESULTADO), os.path.join(dirp, dirct, RESULTADO)))
    print('-----------------------------------------------------------')
    

