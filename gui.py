import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from classes import *

class Main_GUI:
    def __init__(self):
        self.available_things = ['Resitance','Dependent Current Source','Independent Current Source','Dependent Voltage Source','Independent Voltage Source','Wire']
        self.parts = []
        print('window is up and ready!')
        self.create_main_window()
    
    def sel(self):
        selection = "You selected the option " + str(self.string_var.get())
        print(selection)
    
    def place_part(self):
        #TODO: place the part On the Board!
        part_mode = self.string_var.get()
        if (part_mode == 'Resistance'):
            self.parts.append(Resistance(int(self.entry_start.get()),int(self.entry_end.get()),float(self.entry_value.get())))
        elif (part_mode == 'Dependent Current Source'):
            self.parts.append(DependentCurrentSource(int(self.entry_start.get()),int(self.entry_end.get()),self.entry_source.get(),0,float(self.entry_value.get())))
        elif (part_mode == 'Independent Current Source'):
            self.parts.append(IndependentCurrentSource(int(self.entry_start.get()),int(self.entry_end.get()),float(self.entry_value.get())))
        elif (part_mode == 'Dependent Voltage Source'):
            self.parts.append(DependentCurrentSource(int(self.entry_start.get()),int(self.entry_end.get()),self.entry_source.get(),0,float(self.entry_value.get())))
        elif (part_mode == 'Independent Voltage Source'):
            self.parts.append(IndependentVoltagetSource(int(self.entry_start.get()),int(self.entry_end.get()),float(self.entry_value.get())))
        elif (part_mode == 'Wire'):
            self.parts.append(Wire(int(self.entry_start.get()),int(self.entry_end.get())))
        else:
            print('You Have to Select a Part!')
        print('Placed ' + str(part_mode))
        self.place_window.destroy()

    def open_place_part_window(self):
        self.place_window = tk.Toplevel(self.main_window)
        self.place_window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10], minsize=40, weight=1)
        self.place_window.columnconfigure([0, 1, 2], minsize=100, weight=1)
        i = 0
        for x in self.available_things:
            R = tk.Radiobutton(master=self.place_window, text=x,font=self.text_font,selectcolor= 'black', variable=self.string_var, value=x,command=self.sel)
            R.grid(row = i)
            i += 1

        lable_start = tk.Label(master= self.place_window,text = 'Starting Point = ',font = self.text_font)
        lable_start.grid(row = i, column = 0)
        self.entry_start = tk.Entry(master=self.place_window)
        self.entry_start.grid(row = i,column = 1)

        lable_end = tk.Label(master= self.place_window,text = 'Ending Point = ',font = self.text_font)
        lable_end.grid(row = i+1, column = 0)
        self.entry_end = tk.Entry(master=self.place_window)
        self.entry_end.grid(row = i+1,column = 1)

        lable_value = tk.Label(master= self.place_window,text = 'Value = ',font = self.text_font)
        lable_value.grid(row = i+2, column = 0)
        self.entry_value = tk.Entry(master=self.place_window)
        self.entry_value.grid(row = i+2,column = 1)

        lable_source = tk.Label(master= self.place_window,text = 'Value Source(only fill for Dependent sources) = ',font = self.text_font)
        lable_source.grid(row = i+3, column = 0)
        self.entry_source = tk.Entry(master=self.place_window)
        self.entry_source.grid(row = i+3,column = 1)
        
        place_button = tk.Button(master= self.place_window,text='Place Part',command=self.place_part)
        place_button.grid(row = i+4,column = 1)
        

    def create_main_window(self):
        self.main_window = tk.Tk()
        self.string_var = StringVar()
        self.text_font = tkFont.Font(family="Lucida Grande", size=10)
        self.font = tkFont.Font(family="Lucida Grande", size=60)
        self.main_window.rowconfigure([0,1,2,3], minsize=150, weight=1)
        self.main_window.columnconfigure([0, 1, 2], minsize=200, weight=1)
        self.dots = []
        for i in range(9):
            self.dots.append(tk.Label(master=self.main_window, text=".",font = self.font))
            self.dots[i].grid(row = int(i/3), column =int(i%3))
        self.place_button = tk.Button(master=self.main_window, text="Place Part", command=self.open_place_part_window)
        self.place_button.grid(row=3, column=0)
        self.analyze_button = tk.Button(master=self.main_window, text="Analyze", command=self.analyze)
        self.analyze_button.grid(row=3, column=2)
        self.main_window.mainloop()

    def analyze(self):
        print('Analyzing...')
        #TODO:complete here

g = Main_GUI()

