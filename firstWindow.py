# #?window
#!negozio!
#*inserire, modificare e togliere elementi del negozio
#*conto(mostra i prodotti con i loro prezzi, in basso il totale)<--utente che compra
#& https://www.delftstack.com/it/howto/python-tkinter/how-to-get-the-input-from-tkinter-text-box/    #!come ottenere i dati da un input


from ast import main
from tkinter import *
import tkinter as tk

class principale:
    def __init__(self, window):
        """
        """
        self.window = window

    def canvas(self):
        """
        ^ canvas creation
        """
        canvas1 = tk.Canvas(self.window, width = 350, height = 250,  relief = 'raised')
        canvas1.grid(padx=75)
        
    def grafica(self):
        """
        ^ function that deals with the graphics of the window
        """
        self.window.title("First Window") #! set window title
        self.window.configure(bg='orange') #! set window background color
        self.window.geometry('500x400') #! window size
        self.window.resizable(False, False) #! you cannot change the size of the window
        self.window.iconbitmap("icona.ico") #! icon window

    """def centro(window):
        
        #^ opens the window in the center of the desktop
    
        winWidth = window.winfo_reqwidth()
        winwHeight = window.winfo_reqheight()
        posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
        posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
        window.geometry("+{}+{}".format(posRight, posDown))"""

    def label(self, tk, panel):
        """
        ^ label creation
        """
        label1 = tk.Label(self.window, text='Scegli i prodotti')
        label1.config(font=('helvetica', 14, 'bold'),fg="orange")
        panel.create_window(180, 20, window=label1)                     #& non funziona il label dopo il passaggio a classe!
        
    def _input(self):
        """
        """

    def button(self):
        """
        ^ button creation
        """
        button1 = tk.Button(self.window, text='Pagamento',width = 10, height = 3,  font=('helvetica', 12, 'bold'))
        button1.grid(row=1, column=0, sticky="S", pady=40)

        button2 = tk.Button(self.window, text='Carrello',width = 10, height = 3,  font=('helvetica', 12, 'bold'))
        button2.grid(row=1, column=0, sticky="E", pady=40, padx=40)

        button3 = tk.Button(self.window, text='Conatattaci',width = 10, height = 3,  font=('helvetica', 12, 'bold'))
        button3.grid(row=1, column=0, sticky="W", pady=40, padx=40)

        button4 = tk.Button(self.window, text='Alimentazione',width = 15, height = 3, bg='orange', font=('helvetica', 10, 'bold'))
        button4.grid(row=0, column=0, sticky="W", padx=80)
        
        button5 = tk.Button(self.window, text='Sport',width = 15, height = 3, bg='orange', font=('helvetica', 10, 'bold'))
        button5.grid(row=0, column=0, sticky="E", padx=80)

        button6 = tk.Button(self.window, text='abbigliamento',width = 15, height = 3, bg='orange', font=('helvetica', 10, 'bold'))
        button6.grid(row=0, column=0, sticky="S", pady=10)


window = tk.Tk() #! declare the window
w = principale(window) #! call class
#!calls functions
w.grafica()
c = w.canvas()
#?w.label(tk, c)
w.button()

window.mainloop()