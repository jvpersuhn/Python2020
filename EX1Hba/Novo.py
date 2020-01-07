from time import sleep

def Ler():
    f = open('EX1Hba/Terminal.txt','r')
    ret = []
    for i in f:
        ret.append(i.strip())
    
    return ret

def Escrever(lista):
    f = open('EX1Hba/Aviao.txt','w')
    for i in lista:
        f.write(f'{i}\n')

def Mostra(lista):
    s = ''
    for i in range(0,len(lista)):
        if i == 0:
            s += (f'{lista[i]}')
        else:
            s += (f',{lista[i]}')
    print(s)

def Movimento():
    print('Smart Fortwo saindo...')
    #sleep(2.0)
    print('...\n...Smart Fortwo chegou.\n')
    #sleep(2.0)

def ida(p1, p2, Terminal, Aviao):
    print(f'Terminal:')
    Mostra(Terminal)
    print(f'Embarcando: \n{Terminal[p1]} e {Terminal[p2]}')
    Movimento()
    Aviao.append(Terminal[p1])
    Aviao.append(Terminal[p2])
    Terminal.remove(Terminal[p2])
    Terminal.remove(Terminal[p1])

def volta(p1, Aviao, Terminal):
    print(f'Avião:')
    Mostra(Aviao)
    print(f'Embarcando: \n{Aviao[p1]}')
    Movimento()
    Terminal.insert(0,Aviao[p1])
    Aviao.remove(Aviao[p1])

Terminal = Ler()
Aviao = []

for i in range(0,2):
    ida(0,1,Terminal,Aviao)
    volta(i,Aviao,Terminal)

ida(0,1,Terminal,Aviao)
volta(3,Aviao,Terminal)

for i in range(0,2):
    ida(0,1,Terminal,Aviao)
    volta(3 + i,Aviao,Terminal)

ida(1,2,Terminal,Aviao)
volta(2,Aviao,Terminal)

ida(0,1,Terminal,Aviao)
print('Avião:')
Mostra(Aviao)

Escrever(Aviao)