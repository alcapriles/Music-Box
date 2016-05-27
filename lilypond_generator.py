# -*- coding: utf-8 -*-
"""
Created on Mon May  9 19:18:06 2016

@author: Ana Capriles
"""

import os

def abrir_partitura():
    os.startfile('teste.ly', '--png')

    while True:
        if os.path.isfile('teste.pdf'):
            os.startfile('teste.pdf')
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