import time

def LeiaMatrizLocal(NomeArquivo):
    try: arq=open(NomeArquivo,'r')
    except: return []
    Matriz=[]
    for linha in arq:
        Matriz+=[linha.split()]
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            try: Matriz[i][j]=int(Matriz[i][j])
            except: return []
            if Matriz[i][j]>9 or Matriz[i][j]<0: return[]
        if len(Matriz[i])!=9: return []
    if len(Matriz)!=9: return []       
    arq.close()
    return Matriz

def Sudoku(Mat,Lin=0,Col=0):
    global cont
    if Mat[Lin][Col]==0:
        for d in range(1,10):
            l=ProcuraElementoLinha(Mat,Lin,d)
            c=ProcuraElementoColuna(Mat,Col,d)
            q=ProcuraElementoQuadrado(Mat,Lin,Col,d)
            if (l,c)==(-1,-1) and q==(-1,-1):
                Mat[Lin][Col]=d
                if Lin==8 and Col==8:
                    if TestaMatrizPreenchida(Mat)=='false': print('Matriz completa inconsistente.')
                    else:
                        cont+=1
                        print('Matriz completa e consistente nº%s.' %(cont))
                    ImprimaMatriz(Mat)
                else:
                    if Col!=8: Sudoku(Mat,Lin,Col+1)
                    else: Sudoku(Mat,Lin+1,0)
            Mat[Lin][Col]=0
    else:
        if Lin==8 and Col==8:
            if TestaMatrizPreenchida(Mat)=='false': print('Matriz completa inconsistente.')
            else:
                cont+=1
                print('Matriz completa e consistente nº%s' %(cont))
            ImprimaMatriz(Mat)
        else:
            if Col!=8: Sudoku(Mat,Lin,Col+1)
            else: Sudoku(Mat,Lin+1,0)

def ImprimaMatriz(Mat):
    Matriz=''
    for i in range(len(Mat)):
        for j in range(len(Mat[i])):
            Matriz+='%s ' %(Mat[i][j])
        print(Matriz)
        Matriz=''
    print()

def ProcuraElementoLinha(Mat,L,d):
    conta=0
    for i in range(len(Mat[L])):
        if Mat[L][i]==d:
            conta+=1
            pos=i        
    if conta==1: return pos
    if conta==0: return -1
    return 'erro'

def ProcuraElementoColuna(Mat,C,d):
    conta=0
    for j in range(len(Mat)):
        if Mat[j][C]==d:
            conta+=1
            pos=j
    if conta==1: return pos
    if conta==0: return -1
    return 'erro'

def ProcuraElementoQuadrado(Mat,L,C,d):
    conta=0
    l,c=3,3
    if (L+1)/3<=1: l=0
    if (L+1)/3>2: l=6
    if (C+1)/3<=1: c=0
    if (C+1)/3>2: c=6
    for i in range(3):
        for j in range(3):
            if Mat[l+i][c+j]==d:
                conta+=1
                pos=(l+i,c+j)
    if conta==1: return pos
    if conta==0: return (-1,-1)
    return 'erro'

def TestaMatrizPreenchida(Mat):
    for d in range(9):
        for k in range(9):
            if ProcuraElementoLinha(Mat,k,d+1)==-1: return 'false'
            if ProcuraElementoColuna(Mat,k,d+1)==-1: return 'false'
        for i in range(3):
            for j in range(3):
                if ProcuraElementoQuadrado(Mat,3*i,3*j,d+1)==(-1,1):  return 'false'
    return 'true'

def TestaMatrizLida(Mat):
    if Mat==[]: return 'false'
    for d in range(1,10):
        for k in range(9):
            if ProcuraElementoLinha(Mat,k,d)=='erro': return 'false'
            if ProcuraElementoColuna(Mat,k,d)=='erro': return 'false'
        for i in range(3):
            for j in range(3):
                if ProcuraElementoQuadrado(Mat,i,j,d)=='erro': return 'false'
    return 'true'

cont=0
def Main():
    global cont
    print('Entre com o nome do arquivo:')
    Arquivo=str(input())
    if Arquivo=='Fim' or Arquivo=='fim': return
    tempo1=time.time()
    Matriz=LeiaMatrizLocal(Arquivo)
    if TestaMatrizLida(Matriz)=='false':
        print('Matriz inconsistente.')
        Main()
        return
    print('Matriz inicial')
    ImprimaMatriz(Matriz)
    Sudoku(Matriz)
    print('O sudoku de entrada possui %s soluções.' %(cont))
    tempo2=time.time()
    tempo=(tempo2-tempo1)-(tempo2-tempo1)%0.001
    print('O tempo decorrido foi de %s segundos.' %(tempo))
    cont=0
    Main()

Main()
