import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess
import os
import chroma
import recorder

class App:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Music Box')
        self.window.geometry("800x800")
        self.window.rowconfigure(0, minsize=200)
        self.window.rowconfigure(1, minsize=200)
        self.window.rowconfigure(2, minsize=200)
        self.window.rowconfigure(3, minsize=200)
        self.window.columnconfigure(0, minsize=200)
        self.window.columnconfigure(1, minsize=200)
        self.window.configure(background='white')
        
        botao = tk.Button(self.window)
        botao.configure(text='Mostrar Partitura', font="Times 14 bold")
        botao.configure(command=self.abrir_partitura)
        botao.grid(row=3, column=0)
        
        botao2 = tk.Button(self.window)
        botao2.configure(text='Gerar Partitura', font="Times 14 bold")
        botao2.configure(command=self.botao_chromagram_clicado)
        botao2.grid(row=2, column=0)
        
        botao3 = tk.Button(self.window)
        botao3.configure(text='Gravar', font="Times 14 bold")
        botao3.configure(command=self.gravar)
        botao3.grid(row=1, column=0)
        
        botao4 = tk.Button(self.window)
        botao4.configure(text='Escolher arquivo', font="Times 14 bold")
        botao4.configure(command = self.escolher_arquivo)
        botao4.grid(row=0, column=0)
        
    def botao_chromagram_clicado(self):
        C = chroma.make_chroma(self.path)
        nots = chroma.find_notes2(C)
        updated_nots = chroma.update_notes(nots)
        d = chroma.remake_dict(updated_nots)
        the_end = chroma.make_input(d)
        chroma.save_lilypond(the_end)

    def gerar_partitura(self):
        lilypond = r"C:\Program Files (x86)\LilyPond\usr\bin\lilypond.exe"
        subprocess.run([lilypond, "--png", "teste.ly"])
        
        while True:
            if os.path.isfile('teste.png'):
                return os.path.abspath('teste.png')    
        
    def abrir_partitura(self):
        path = self.gerar_partitura()
        img = ImageTk.PhotoImage(Image.open(path))
        panel = tk.Label(self.window, image = img)
        panel.image = img        
        panel.grid(column = 1, row = 0, columnspan=3, rowspan=3)
        
    def escolher_arquivo(self):     
        self.path = filedialog.askopenfilename(defaultextension='wav')
        
    def iniciar(self):
        self.window.mainloop()
        
    def gravar(self):
        f = open('output.wav','w')
        path = f.name
        f.close()
        recorder.record(path)
        self.path = filedialog.asksaveasfilename(defaultextension='wav')
        os.rename(path, self.path)

musicBox = App()
musicBox.iniciar()

