import tkinter as tk
import os
import subprocess
import lilypond_generator
import chromagram

class Example:
    def __init__(self):
        self.lilypond = lilypond_generator.Lilypond()
        self.arquivo = self.lilypond.arquivo
        self.button_status = 'pause'        
        
        self.window = tk.Tk()
        
        self.window.title("MusicBox")
        self.window.geometry("600x400")
        self.window.rowconfigure(0, minsize=100,weight=1)
        self.window.columnconfigure(0, minsize=100,weight=1)
        self.window.columnconfigure(1, minsize=100,weight=1)
        self.window.columnconfigure(2, minsize=200,weight=1)
        self.window.columnconfigure(3, minsize=450, weight=1)        
        
        self.play = tk.PhotoImage(file = 'Icone_play.png')
        self.pause = tk.PhotoImage(file = 'Icone_pause.png')
        self.button_gravar = tk.Button(self.window, image = self.pause)
        self.button_gravar.grid(row=1, column= 1, sticky= 'nsew') 
        self.button_gravar.configure(text= 'Pause')
        self.button_gravar.configure(command= self.play_pause)  
        
        self.label_partitura = tk.Label(self.window)
        self.label_partitura.configure(font= 'Courirer 16 bold')
        self.label_partitura.configure(text= 'Arquivo gerado com a partitura')
        self.label_partitura.grid(row=2, column= 3, sticky= 'nsew')
        
        self.label_arquivo = tk.Label(self.window)
        self.label_arquivo.configure(font= 'Courirer 14')
        self.label_arquivo.configure(text= '')
        self.label_arquivo.grid(row=1, column= 3, sticky= 'nsew')
        
    def iniciar(self):
        self.window.mainloop()
    
    def play_pause(self):
        
        if (self.button_status == 'pause'):
            self.button_gravar = tk.Button(self.window, image = self.play)
            self.button_status = 'play'
            print('1')
        elif (self.button_status == 'play'):
            self.button_gravar = tk.Button(self.window, image = self.pause)
            self.button_status = 'pause'
            self.gerar_cromagrama()
            self.nome_arquivo()
            print('2')
            
    def gerar_cromagrama(self): 
        
    def nome_arquivo(self):
        self.label_arquivo = tk.Label(self.window)
        self.label_arquivo.configure(font= 'Courirer 14')
        self.label_arquivo.configure(text= self.arquivo)
        self.label_arquivo.grid(row=1, column= 3, sticky= 'nsew')
    
        
app= Example()
app.iniciar()