import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from classes import *
from PIL import Image, ImageTk
import numpy as np

class Main_GUI:
    def __init__(self):
        self.available_things = ['Resistance','Dependent Current Source','Independent Current Source','Dependent Voltage Source','Independent Voltage Source','Wire']
        self.parts = []
        print('window is up and ready!')
        self.create_main_window()
    
    def sel(self):
        selection = "You selected the option " + str(self.string_var.get())
        print(selection)
    
    def draw_part(self):
        print('drawing...')
        part = self.parts[-1]
        path = part.type + '.png'
        d = 0
        d_horiz_verti = 0
        image = Image.open(path)
        image = image.resize((120, 100), Image.ANTIALIAS)
        if (part.start == part.end - 1):
            d_horiz_verti = 0
            d = 2*int(part.start/3) + (part.start%3) - 1
            print('No Rotate needed.')
        elif (part.start - 1 == part.end):
            d_horiz_verti = 0
            d = 2*int(part.end/3) + (part.end%3) - 1
            image = image.transpose(Image.ROTATE_180)
        elif (part.start == part.end - 3):
            d_horiz_verti = 1
            d = part.start - 1
            image = image.transpose(Image.ROTATE_270)
        elif (part.start - 3 == part.end):
            d_horiz_verti = 1
            d = part.end - 1
            image = image.transpose(Image.ROTATE_90)
        img = ImageTk.PhotoImage(image)
        if (d_horiz_verti == 0):
            self.place_locals_horiz[d].configure(image = img)
            self.place_locals_horiz[d].image = img
        else:
            self.place_locals_verti[d].configure(image = img)
            self.place_locals_verti[d].image = img

        
    def place_part(self):
        part_mode = self.string_var.get()
        if (not (part_mode in self.available_things)):
            print('You Have to Select a Part!')
            return
        self.parts.append(Part(part_mode,int(self.entry_start.get()),int(self.entry_end.get()),value=float(self.entry_value.get()),value_source=self.entry_source.get()))
        self.draw_part()
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
        self.main_window.title('Main Window')
        self.string_var = StringVar()
        self.text_font = tkFont.Font(family="Lucida Grande", size=10)
        self.font = tkFont.Font(family="Lucida Grande", size=60)
        self.main_window.rowconfigure([0,1,2,3,4,5], minsize=100, weight=1)
        self.main_window.columnconfigure([0, 1, 2,3,4], minsize=120, weight=1)
        self.dots = []
        self.place_locals_horiz = []
        self.place_locals_verti = []
        for i in range(9):
            self.dots.append(tk.Label(master=self.main_window, text=".",font = self.font))
            self.dots[i].grid(row = int(i/3)*2, column =int(i%3)*2)
        imh = PhotoImage(file='Wire.png')
        imv = PhotoImage(file='WireFlipped.png')
        for i in range(6):
            self.place_locals_horiz.append(Label(master=self.main_window,image = imh))
            self.place_locals_horiz[i].grid(row = int(i/2) * 2,column = ((i%2) *2) + 1,sticky = NSEW)
        for i in range(6):
            self.place_locals_verti.append(Label(master=self.main_window,image = imv))
            self.place_locals_verti[i].grid(row =(int(i/3) * 2) + 1,column = int(i%3) * 2,sticky = NSEW)
        self.place_button = tk.Button(master=self.main_window, text="Place Part", command=self.open_place_part_window)
        self.place_button.grid(row=5, column=1,sticky = NSEW)
        self.analyze_button = tk.Button(master=self.main_window, text="Analyze", command=self.analyze)
        self.analyze_button.grid(row=5, column=3,sticky = NSEW)
        self.main_window.mainloop()

    def analyze(self):
        print('Analyzing...')
        R1 = self.parts[0].value
        R2 = self.parts[1].value
        R3 = self.parts[2].value
        I1 = self.parts[3].value
        I2 = self.parts[4].value
        I3 = self.parts[5].value
        V = self.parts[6].value
        # for voltage of each nodes

        # V4, V5, V6
        a = np.array([[1/R3, -1/R1, 1/R1], [0, 1/R1+1/R2, -1/R1], [-1, 0, 1]])
        b = np.array([I2, I1+I3, V])
        x = np.linalg.solve(a,b)
        print('V1 = ' + str(x[2]))
        print('V2 = ' + str(x[2]))
        print('V3 = ' + str(x[0]))
        print('V4 = ' + str(x[2]))
        print('V5 = ' + str(x[1]))
        print('V6 = ' + str(x[0]))
        print('V7 = ' + str(0))
        print('V8 = ' + str(0))
        print('V9 = ' + str(0))
        print('Analyze is over.')

g = Main_GUI()

