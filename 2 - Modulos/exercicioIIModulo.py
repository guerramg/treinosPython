import os

def desliga1Hora():
    os.system('shutdown -s -t 3600')
    print ('Sua maquina irá desligar em 1 hora.')
    
def desliga30Minutos():
    os.system('shutdown -s -t 1800')
    print ('sua maquina irá desligar em 30 minutos.')
    
def cancelaDesligamento():
    os.system('shutdown -a')
    print ('o desligamento foi cancelado com sucesso.')