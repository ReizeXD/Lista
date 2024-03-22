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
        print()




def selection(lista):
    n=len(lista)
    for c in range(0,n-1):
        menor=c
        for x in range(c+1,n):
            if lista[menor]>lista[x]:
                menor=x
        lista[c],lista[menor]=lista[menor],lista[c]
    return lista
def inserir(lista):
    lista=selection(lista)
    c1=Lista()
    for c in lista:
        c1.append(c)
    c1.printe()
lista=[6, 4, 3, 7, 8, 2]
inserir(lista)
""" [2, 3, 4, 6, 7, 8] """
        