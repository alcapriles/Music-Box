from tkinter import Tk, Frame, Checkbutton
from tkinter import BooleanVar, BOTH
import tkinter as tk

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
        
    def initUI(self):
        self.window = tk.Tk()
        self.window.title("MusicBox")
        self.window.geometry("600x400")
        self.window.rowconfigure(0, minsize=100,weight=1)
        self.window.columnconfigure(0, minsize=100,weight=1)
        self.window.columnconfigure(1, minsize=100,weight=1)
      
        self.parent.title("Checkbutton")

        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()
        
        cb = Checkbutton(self, text="Show title",
            variable=self.var, command=self.onClick)
        cb.select()
        cb.place(x=50, y=50)
        

    def onClick(self):
       
        if self.var.get() == True:
            self.master.title("Checkbutton")
        else:
            self.master.title("")


def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  