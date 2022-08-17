from tkinter import *
import tkinter as tk

class ThirdWindow():

    def __init__(self, window3):
        """
        """
        self.window3 = window3

    def grafica3(self):
        """
        ^ function that deals with the graphics of the secondWindow
        """
        self.window3.title("Alimentazione") #! set window title
        self.window3.configure(bg='grey') #! set window background color
        self.window3.geometry('500x400') #! window size
        self.window3.resizable(False, False) #! you cannot change the size of the window
        self.window3.iconbitmap("icona.ico") #! icon window

    def ListBox(self):
        """
        ^ listBox creation
        """
        lista = ["mela", "banana", "mela", "ciliegia", "pera", "mela", "pera", "pera",  "ciliegia", "pera", "fragola"]
        lb1 = tk.Listbox(self.window3, selectmode=EXTENDED, height=10, width=50,font=('helvetica', 13))
        for i in range(len(lista)):
            lb1.insert(i, lista[i])
            print(i)
        lb1.pack()
