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
import time

class App:
    
    def __init__(self):
        self.loading = False     
        self.load = 1
        
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
        
        self.tela_loading()
        
        
    def tela_loading(self):
        while (self.loading == True):
            self.window_loading = tk.Tk()
            C = tk.Canvas(self.window_loading, bg="grey", height=250, width=260)
            
            coord = 10, 50, 240, 210
            arc = C.create_arc(coord, start=0, extent = self.load, fill="green")
        
            C.pack()
            
            if (self.load <= 359):
                arc = C.create_arc(coord, start=0, extent = self.load, fill="green")
                self.load+=1
            self.load=1
    
    def tempo_loading(self,x,y):
        z = 1
        if (y == 0):
            z=z+1
        else:
            z = x-y
        time.sleep(z)
        
    def botao_chromagram_clicado(self):
        C = chroma.make_chroma()
        nots = chroma.find_notes2(C)
        updated_nots = chroma.update_notes(nots)
        d = chroma.remake_dict(updated_nots)
        the_end = chroma.make_input(d)
        chroma.save_lilypond(the_end)

#    def botao_chromagram_clicado(self):
#        x=0
#        y=0
#        self.loading = True
#        x = time.perf_counter()
#        
#        while (x-y == x):
#            self.tempo_loading(x,y)
#            C = chroma.make_chroma()
#            nots = chroma.find_notes2(C)
#            inp = chroma.make_input(nots)
#            chroma.save_lilypond(inp)
#            y = time.perf_counter()
#
#
#        self.loading = False
#        self.load=1
      
    def iniciar(self):
        self.window.mainloop()

musicBox = App()
musicBox.iniciar()


''' 

Código da tela loading funcionando

def tela_loading():
    top = tkinter.Tk()
    
    C = tkinter.Canvas(top, bg="grey", height=250, width=260)
    
    coord = 10, 50, 240, 210
    arc = C.create_arc(coord, start=0, extent=load, fill="green")

    C.pack()

    while (loading == True):
        if (load <= 359):    
            load+=1
        load=1
        
tela_loading()
top.mainloop()
'''