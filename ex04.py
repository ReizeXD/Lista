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
    def insert(self,valor,pos):
        if pos>=0 and pos<self.tamanho:
            if self.estavazia() and self.tamanho==pos:
                self.append(valor)
            else:
                c=Celula(valor)
                if pos==0:
                    c.proximo=self.inicio
                    self.inico=c
                else:
                    aux=self.inicio
                    i=0
                    while i<pos-1:
                        aux=aux.proximo
                        i+=1
                    c.proximo=aux.proximo
                    aux.proximo=c
                self.fim=c
                self.tamanho+=1


    def pop(self,pos=0):
        if pos>=0 and pos<self.tamanho:
            if pos==0:
                c=self.inicio
                self.inicio=self.inicio.proximo
            else:
                aux=self.inicio
                i=0
                while i<pos-1:
                    aux=aux.proximo
                    i+=1
                c=aux.proximo
                aux.proximo=c.proximo
            self.fim=aux
            valor=c.valor
            del c
            self.tamanho-=1
            return valor
    def printe(self):
        aux=self.inicio
        while aux!=None:
            print(aux.valor,end=" ")
            aux=aux.proximo
        print()



def palavras(var,sub_var):
    c1=Lista()
    c2=Lista()
    for c in var:
        c1.append(c)
    for c in sub_var:
        c2.append(c)
    
    aux1=c1.inicio
    aux2=c2.inicio
    tam=0
    condicao=False
    c1.printe()
    c2.printe()

    for i in range(c1.tamanho):
        print(aux1.valor,aux2.valor)
        if aux1.valor!=aux2.valor:
            if tam==0:
                aux1=aux1.proximo
            else:
                aux2=c2.inicio
                print(aux2.valor)
                tam=0
        else:
            aux1=aux1.proximo
            aux2=aux2.proximo
            tam=1
        try:
            print(aux1.proximo.valor)
        except:
            print("proximo é None")
        if aux2.proximo==None and tam==1:
            condicao=True
            break
    return condicao
""" encadadae
        dae """
print(palavras('encadadae','ena'))           


