import os

def abrir_partitura():
    os.startfile('teste.ly', '--png')

    while True:
        if os.path.isfile('teste.png'):
            os.startfile('teste.png')
            break
        
    '''
    Opção de salvar a partitura:
    image = ""
    msg   = "Partitura"
    choices = ["Continuar", "Sair"]
    reply=buttonbox(msg,image=image,choices=choices)
    
    if (reply):
        title = 'Salvar'
        filesavebox(msg=None, title = title, default=None)
    '''