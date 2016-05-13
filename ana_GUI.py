# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:45:50 2016

@author: Ana Capriles
"""

import tkinter as tk
import chromagram
import lilypond_generator

class App:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Music Box')
        
        botao = tk.Button(self.window)
        botao.configure(text='Gerar Cromagrama')
        botao.configure(command=chromagram.chromagram())
        botao.grid()
        
        botao2 = tk.Button(self.window)
        botao2.configure(text='Gerar Partitura')
        botao2.configure(command=lilypond_generator.abrir_partitura())
        botao2.grid()        

    def iniciar(self):
        self.window.mainloop()

musicBox = App()
musicBox.iniciar()