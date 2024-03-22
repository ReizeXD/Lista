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
    def verrepet(self,valor):
        aux=self.inicio
        condicao=False
        while aux!=None:
            if aux.valor==valor:
                condicao=True
                break
            aux=aux.proximo
        return condicao
    def printe(self):
        aux=self.inicio
        while aux!=None:
            print(aux.valor,end=" ")
            aux=aux.proximo
        print()

def inserir(lista):
    c1=Lista()
    for c in lista:
        if not c1.verrepet(c):
            c1.append(c)
    c1.printe()
inserir([1, 1, 2, 3, 4, 4, 5, 6, 6])

