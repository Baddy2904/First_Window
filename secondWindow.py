# #!

from tkinter import *
import tkinter as ttk

class SecondWindow():

    def __init__(self, window2):
        """
        ^
        """
        self.window2 = window2

    def grafica2(self):
        """
        ^ function that deals with the graphics of the secondWindow
        """
        self.window2.title("Pagamento") #! set window title
        self.window2.configure(bg='grey') #! set window background color
        self.window2.geometry('500x400') #! window size
        self.window2.resizable(False, False) #! you cannot change the size of the window
        self.window2.iconbitmap("icona.ico") #! icon window

