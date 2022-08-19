# #!

from tkinter import *
import tkinter as tk

class SellWindow():

    def __init__(self, window,title,listaMateriali,listaPrezzi):
        """
        ^
        """
        window.title(title)#! set window title
        self.window = window
        self.listaMateriali = listaMateriali
        self.listaPrezzi = listaPrezzi
        #self.carrello = []

    def grafica(self):
        """
        ^ function that deals with the graphics of the window
        """
        self.window.configure(bg='grey') #! set window background color
        self.window.geometry('500x400') #! window size
        self.window.resizable(False, False) #! you cannot change the size of the window
        #self.window3.iconbitmap("icona.ico") #! icon window

    def ListBox(self):
        """
        ^ listBox creation
        """
        
        lb1 = tk.Listbox(self.window, selectmode=EXTENDED, height=10, width=50,font=('helvetica', 13))
        #
        for i in range(len(self.listaMateriali)):
            materiale = "- " + self.listaMateriali[i] + " "*(30 - len(self.listaMateriali[i])) + self.listaPrezzi[i]+"£"
            lb1.insert(i, materiale)
        lb1.grid()

    def button(self):
        """
        ^ button creation
        """
        button = tk.Button(
            self.window,
            text='Aggiungi al carrello',
            width = 15,
            height = 3,
            bg="purple",
            fg="black",
            activebackground="purple",
            activeforeground="black",
            font=('helvetica', 12, 'bold'),
            #command=carrello
            )

        button.grid(
            row=1,
            column=0,
            sticky="S",
            pady=40)

#def carrello(self):
        
        #^adding the selected items to the bought item list
        
