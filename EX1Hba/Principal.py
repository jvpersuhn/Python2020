import time

def Mostra(lista):
    s = ''
    for i in range(0,len(lista)):
        if i == 0:
            s += (f'{lista[i]}')
        else:
            s += (f',{lista[i]}')
    print(s)

def Movimento():
    print('ForTwo saindo....')
    time.sleep(2.0)
    print('ForTwo chegou...')

def EmbarqueTerminal(p1,p2,terminal,aviao,inverter = False):
    print(f'Embarcando: {terminal[p1]} , {terminal[p2]}')
    temp = terminal[p1]
    aviao.append(terminal[p2])
    if inverter:
        terminal.remove(terminal[p1])
        terminal.remove(terminal[p2])
    else:
        terminal.remove(terminal[p2])
        terminal.remove(terminal[p1])
    print('Terminal: ')
    Mostra(terminal)
    Movimento()
    terminal.insert(0,temp)
    print('Avião: ')
    Mostra(aviao)
    print(f'Voltando: {terminal[p1]}')

def QuebraLinha():
    print('\n')

def Policial(terminal,aviao):
    print(f'Embarcando: {terminal[1]} , {terminal[2]}')
    aviao.append(terminal[1])
    aviao.append(terminal[2])
    terminal.remove('Policial')
    terminal.remove('ladrao')
    terminal.append(aviao[2])
    aviao.remove('Piloto')
    Movimento()
    print('Voltando: Piloto')
    Movimento()
    print('Avião: ')
    Mostra(aviao)
    QuebraLinha()

def Final(terminal,aviao):
    print(f'Embarcando: {terminal[0]} , {terminal[1]}')
    Movimento()
    aviao.append(terminal[0])
    aviao.append(terminal[1])
    terminal.remove('Piloto')
    terminal.remove('ChefeSerVoo')
    print('Terminal: ')
    Mostra(terminal)
    print('Avião: ')
    Mostra(aviao)
    QuebraLinha()

terminal = ['Piloto','Oficial1','Oficial2','ChefeSerVoo','com1','com2','Policial','ladrao']
aviao = []

for i in range(0,2):
    EmbarqueTerminal(0,1,terminal,aviao)
    QuebraLinha()

EmbarqueTerminal(1,0,terminal,aviao,inverter=True)

for i in range(0,2):
    EmbarqueTerminal(0,1,terminal,aviao)
    QuebraLinha()

Policial(terminal,aviao)
Final(terminal,aviao)

