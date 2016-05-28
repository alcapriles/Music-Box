import tkinter as tk
import chroma
import lilypond_generator
import recorder
from tkinter import filedialog

class App:
    
    def __init__(self):
        self.escolheu_arquivo = False        
        self.path = ''        
        
        self.window = tk.Tk()
        self.window.title('Music Box')
        self.window.geometry("400x200")
        self.window.rowconfigure(0, minsize=100)
        self.window.rowconfigure(1, minsize=100)
        self.window.columnconfigure(0, minsize=200)
        self.window.columnconfigure(1, minsize=200)

        
        botao = tk.Button(self.window)
        botao.configure(text='Mostrar Partitura', font="Times 14 bold")
        botao.configure(command=lilypond_generator.abrir_partitura)
        botao.grid(row=0, column=0, sticky ='nsew')
        
        botao2 = tk.Button(self.window)
        botao2.configure(text='Gerar Partitura', font="Times 14 bold")
        botao2.configure(command=self.botao_chromagram_clicado)
        botao2.grid(row=0, column=1, sticky ='nsew')
        
        botao3 = tk.Button(self.window)
        botao3.configure(text='Gravar', font="Times 14 bold")
        botao3.configure(command=recorder.record)
        botao3.grid(row=1, column=0, sticky ='nsew')
        
        botao4 = tk.Button(self.window)
        botao4.configure(text='Escolher arquivo', font="Times 14 bold")
        botao4.configure(command = self.escolher_arquivo)
        botao4.grid(row=1, column=1, sticky ='nsew')
        
    def botao_chromagram_clicado(self):
        C = chroma.make_chroma()
        nots = chroma.find_notes2(C)
        updated_nots = chroma.update_notes(nots)
        d = chroma.remake_dict(updated_nots)
        the_end = chroma.make_input(d)
        chroma.save_lilypond(the_end)

      
    def escolher_arquivo(self):     
        self.path = filedialog.askopenfiles(mode='r') 
        
    def iniciar(self):
        self.window.mainloop()

musicBox = App()
musicBox.iniciar()

