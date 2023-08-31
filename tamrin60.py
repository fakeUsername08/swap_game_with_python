from tkinter import *
import random

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.config(bg='aqua', relief='ridge', border=10)

        self.create()

    def create(self):
        self.btn1 = Button(self, text=1, width=10, height=5, command=lambda:self.swap(self.btn1))
        self.btn2 = Button(self, text=2, width=10, height=5, command=lambda:self.swap(self.btn2))
        self.btn3 = Button(self, text=3, width=10, height=5, command=lambda:self.swap(self.btn3))
        self.btn4 = Button(self, text=4, width=10, height=5, command=lambda:self.swap(self.btn4))
        self.btn5 = Button(self, text=5, width=10, height=5, command=lambda:self.swap(self.btn5))
        self.btn6 = Button(self, text=6, width=10, height=5, command=lambda:self.swap(self.btn6))
        self.btn7 = Button(self, text=7, width=10, height=5, command=lambda:self.swap(self.btn7))
        self.btn8 = Button(self, text=8, width=10, height=5, command=lambda:self.swap(self.btn8))
        self.btn9 = Button(self, text=9, width=10, height=5, command=lambda:self.swap(self.btn9))
        self.btn10 = Button(self, text=10, width=10, height=5, command=lambda:self.swap(self.btn10))
        self.btn11 = Button(self, text=11, width=10, height=5, command=lambda:self.swap(self.btn11))
        self.btn12 = Button(self, text=12, width=10, height=5, command=lambda:self.swap(self.btn12))
        self.btn13 = Button(self, text=13, width=10, height=5, command=lambda:self.swap(self.btn13))
        self.btn14 = Button(self, text=14, width=10, height=5, command=lambda:self.swap(self.btn14))
        self.btn15 = Button(self, text=15, width=10, height=5, command=lambda:self.swap(self.btn15))
        self.btnfree = Button(self, bg='aqua', border=0, width=10, height=5, state='disabled')

        # random grid
        list = [(0,0),(0,1),(0,2),(0,3),
                (1,0),(1,1),(1,2),(1,3),
                (2,0),(2,1),(2,2),(2,3),
                (3,0),(3,1),(3,2),(3,3),]
        random.shuffle(list)

        self.btn1.grid(row=list[0][0], column=list[0][1], padx=30, pady=30)
        self.btn2.grid(row=list[1][0], column=list[1][1], padx=30, pady=30)
        self.btn3.grid(row=list[2][0], column=list[2][1], padx=30, pady=30)
        self.btn4.grid(row=list[3][0], column=list[3][1], padx=30, pady=30)
        self.btn5.grid(row=list[4][0], column=list[4][1], padx=30, pady=30)
        self.btn6.grid(row=list[5][0], column=list[5][1], padx=30, pady=30)
        self.btn7.grid(row=list[6][0], column=list[6][1], padx=30, pady=30)
        self.btn8.grid(row=list[7][0], column=list[7][1], padx=30, pady=30)
        self.btn9.grid(row=list[8][0], column=list[8][1], padx=30, pady=30)
        self.btn10.grid(row=list[9][0], column=list[9][1], padx=30, pady=30)
        self.btn11.grid(row=list[10][0], column=list[10][1], padx=30, pady=30)
        self.btn12.grid(row=list[11][0], column=list[11][1], padx=30, pady=30)
        self.btn13.grid(row=list[12][0], column=list[12][1], padx=30, pady=30)
        self.btn14.grid(row=list[13][0], column=list[13][1], padx=30, pady=30)
        self.btn15.grid(row=list[14][0], column=list[14][1], padx=30, pady=30)
        self.btnfree.grid(row=list[15][0], column=list[15][1], padx=30, pady=30)

    def swap(self, name):
        if self.btnfree.grid_info()['row'] == name.grid_info()['row']:
            if abs(self.btnfree.grid_info()['column'] - name.grid_info()['column']) == 1:
                temp = self.btnfree.grid_info()['column']
                self.btnfree.grid_configure(column=name.grid_info()['column'])
                name.grid_configure(column=temp)

        elif self.btnfree.grid_info()['column'] == name.grid_info()['column']:
            if abs(self.btnfree.grid_info()["row"] - name.grid_info()["row"]) == 1:
                temp = self.btnfree.grid_info()['row']
                self.btnfree.grid_configure(row=name.grid_info()['row'])
                name.grid_configure(row=temp)







App().mainloop()