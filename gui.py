import tkinter as tk
import tkinter.font as tkFont
from tkinter import *

class Main_GUI:
    def __init__(self):
        self.available_things = ['Resitance','Dependent Current Source','independent Current Source','Dependent Voltage Source','independent Voltage Source']
        print('window is up and ready!')
        self.create_main_window()
    
    def sel(self):
        selection = "You selected the option " + str(self.string_var.get())
        print(selection)

    def open_place_part_window(self):
        self.place_window = tk.Toplevel(self.main_window)
        self.place_window.geometry("800x800+500+200")
        for x in self.available_things:
            R = tk.Radiobutton(master=self.place_window, text=x,font=self.text_font,selectcolor= 'black', variable=self.string_var, value=x,command=self.sel)
            R.pack()

    def create_main_window(self):
        self.main_window = tk.Tk()
        self.string_var = StringVar()
        self.text_font = tkFont.Font(family="Lucida Grande", size=18)
        self.font = tkFont.Font(family="Lucida Grande", size=60)
        self.main_window.rowconfigure([0,1,2,3], minsize=150, weight=1)
        self.main_window.columnconfigure([0, 1, 2], minsize=200, weight=1)
        self.dots = []
        for i in range(9):
            self.dots.append(tk.Label(master=self.main_window, text=".",font = self.font))
            self.dots[i].grid(row = int(i/3), column =int(i%3))
        self.button = tk.Button(master=self.main_window, text="Place Part", command=self.open_place_part_window)
        self.button.grid(row=3, column=1, sticky="nsew")
        self.main_window.mainloop()

g = Main_GUI()

