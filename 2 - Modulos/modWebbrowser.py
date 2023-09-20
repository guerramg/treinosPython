import webbrowser

estado = False

while not estado:
    print('0. O que deseja fazer?')
    print('1. abrir google')
    print('2. abrir yahoo')
    print ('3. sair')
    
    escolha = input('>')
    
    if(escolha == '1'):
        webbrowser.open('https://google.com.br')
    elif(escolha == '2'):
        webbrowser.open('http://yahoo.com.br')
    elif(escolha == '3'):
        estado = True