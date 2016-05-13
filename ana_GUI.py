# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:45:50 2016

@author: Ana Capriles
"""

import tkinter as tk
import chromagram
import lilypond_generator
import recorder

class App:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Music Box')
        self.window.geometry("600x600")
        self.window.rowconfigure(0, minsize=200)
        self.window.rowconfigure(1, minsize=200)
        self.window.rowconfigure(2, minsize=200)
        self.window.columnconfigure(0, minsize=600)
        
        botao = tk.Button(self.window)
        botao.configure(text='Mostrar Partitura')
        botao.configure(command=lilypond_generator.abrir_partitura)
        botao.grid(row=0, column=0)
        
        botao2 = tk.Button(self.window)
        botao2.configure(text='Gerar Partitura')
        botao2.configure(command=self.botao_chromagram_clicado)
        botao2.grid(row=1, column=0)
        
        botao = tk.Button(self.window)
        botao.configure(text='Gravar')
        botao.configure(command=recorder.record)
        botao.grid(row=2, column=0)

    def botao_chromagram_clicado(self):
        CS = chromagram.compute_chromagram()
        notas = chromagram.find_notes(CS)
        chromagram.save_lilypond(notas)

    def iniciar(self):
        self.window.mainloop()

musicBox = App()
musicBox.iniciar()