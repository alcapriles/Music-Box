# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:45:50 2016

@author: Ana Capriles
"""

#Para rodar direito os aplicativos padrão precisam ser: .pdf - Navegador(Google Chrome, etc) .ly - Lilypond

import tkinter as tk
import chroma
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
        
        botao3 = tk.Button(self.window)
        botao3.configure(text='Gravar')
        botao3.configure(command=recorder.record)
        botao3.grid(row=2, column=0)

    def botao_chromagram_clicado(self):
        C = chroma.make_chroma()
        nots = chroma.find_notes2(C)
        inp = chroma.make_input(nots)
        chroma.save_lilypond(inp)

    def iniciar(self):
        self.window.mainloop()

musicBox = App()
musicBox.iniciar()