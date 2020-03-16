import time

def main():
    print('Entre com o nome do arquivo de origem:')
    Entrada=input()
    if Entrada=='fim' or Entrada=='Fim': return
    Origem=open(Entrada,'r')
    print('Entre com o nome do arquivo destino:')
    Destino=open(input(),'w')

    TAB=[]
    Contador=0
    for linha in Origem:
        Contador+=1
        linha=linha.replace('\n','')
        TAB+=[linha]
    print()
    print('Quantidade de registros a classificar: %s registros' %Contador)
    print()

    Lista=CopiaLista(TAB) # Executando o método sort() do Python
    t1=time.time()
    ClassMetodoSort(Lista)
    t2=time.time()
    VerifClass(Lista)
    print('Método sort() do Python:',t2-t1,'segundos')

    Lista=CopiaLista(TAB) # Executando o método Quick Recursivo
    t1=time.time()
    ClassQuickRecursivo(Lista,0,len(Lista)-1)
    t2=time.time()
    VerifClass(Lista)
    print('Método Quick Recursivo:',t2-t1,'segundos')
    
    Lista=CopiaLista(TAB) # Executando o método Quick Não Recursivo
    t1=time.time()
    ClassQuickNaoRecursivo(Lista)
    t2=time.time()
    VerifClass(Lista)
    print('Método Quick Não Recursivo:',t2-t1,'segundos')

    print()
    for i in range(Contador):
        Destino.write(Lista[i]+'\n')
    main()

def CopiaLista(Lista):
    Nova=[0]*len(Lista)
    for i in range(len(Lista)):
        Nova[i]=Lista[i]
    return Nova

class PilhaLista(): # Definindo a classe pilha e suas funções
  def __init__(self):
    self.pilha = []
    
  def __len__ (self):
    return len(self.pilha)

  def empty(self):
    return len(self.pilha)==0
  
  def push(self, e):
    self.pilha.append(e)

  def pop(self):
    if self.empty( ):
      raise Empty("Pilha vazia")
    return self.pilha.pop( )

def ClassQuickRecursivo(Lista,Inicio,Fim):
    if Inicio < Fim:
        k=Particiona(Lista,Inicio,Fim)
        ClassQuickRecursivo(Lista,Inicio,k-1)
        ClassQuickRecursivo(Lista,k+1,Fim)

def ClassQuickNaoRecursivo(Lista):
    Pilha=PilhaLista()
    Pilha.push((0,len(Lista)-1))
    while not Pilha.empty():
        Inicio,Fim=Pilha.pop()
        if Fim-Inicio > 0:
            k=Particiona(Lista,Inicio,Fim)
            Pilha.push((Inicio,k-1))
            Pilha.push((k+1,Fim))

def ClassMetodoSort(Lista):
    for i in range(len(Lista)):
        Linha=Lista[i]
        Linha=Linha.split(',')
        Linha[1],Linha[2]=Linha[2],Linha[1]
        Lista[i]=Linha[0]+Linha[1]+Linha[2]
    Lista.sort()

def VerifClass(Lista):
    for i in range(len(Lista)-1):
        if ChecaMaior(Lista[i],Lista[i+1])==2:
            print('Classificação incorreta!')
            return 'false' 
    return 'true'
  
def Particiona(Lista,Inicio,Fim):
    i,j=Inicio,Fim
    Pivo=Lista[Fim]
    while True:
        while i < j and ChecaMaior(Lista[i],Pivo)==1: i+=1
        if i < j:
            Lista[i],Lista[j]=Pivo,Lista[i]
        else: break
        while i < j and ChecaMaior(Lista[j],Pivo)==2: j-=1
        if i < j: Lista[i],Lista[j]=Lista[j],Pivo
        else: break
    return i

def ChecaMaior(A,B):
    A=A.split(',')
    B=B.split(',')
    if A[0]==B[0] and A[2]==B[2]: # Classificação pela data
        A=A[1].split('/')
        B=B[1].split('/')
        if A[2]==B[2]:
            if A[1]==B[1]:
                if int(A[0])<int(B[0]): return 1
                else: return 2
            else:
                if int(A[1])<int(B[1]): return 1
                else: return 2
        else:
            if int(A[2])<int(B[2]): return 1
            else: return 2
        
    elif A[0]==B[0]: # Classificação pela identificação
        if int(A[2])<int(B[2]): return 1
        else: return 2
    else: # Classificação pelo nome
        if A[0]<B[0]: return 1
        else: return 2

main()
