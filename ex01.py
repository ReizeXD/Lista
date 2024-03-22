class Celula:
    valor=None
    proximo=None
    def __init__(self,valor):
        self.valor=valor
class Lista:
    inicio=None
    fim=None
    tamanho=0
    def estavazia(self):
        return self.inicio==None
    def append(self,valor):
        c=Celula(valor)
        if self.estavazia():
            self.inicio=c
        else:
            self.fim.proximo=c
        self.fim=c
        self.tamanho+=1
    def printe(self):
        aux=self.inicio
        while aux!=None:
            print(aux.valor,end=" ")
            aux=aux.proximo

def entrelaçar(lista1,lista2):
    n=len(lista1)
    m=len(lista2)
    soma=n+m
    c1=Lista()
    for i in range(soma):
        if i<n:
            c1.append(lista1[i])
        if i<m:
            c1.append(lista2[i])
        if i==n and i==m:
            break
    c1.printe()
lista1=[1,3,7,9]
lista2=[2,4,6,10]
entrelaçar(lista1,lista2)

