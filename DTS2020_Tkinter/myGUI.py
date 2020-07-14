#myGUI.py
import tkinter as tk
from myFun import htluas
from tkinter import messagebox

def btn_hitung():
    pj = inp1.get()
    tg = inp2.get()

    try:
        pj = float(pj)
        tg = float(tg)
        lbl3['text'] = str(htluas(pj,tg))
    except ValueError:
        messagebox.showinfo("Alert Message", "Angka, bro!")
        
     
wdw = tk.Tk()
wdw.title("Ini GUI") #mengubah nama jendela

inp1 = tk.Entry(wdw)
inp1.insert(0,0.0)
inp1.grid(row=0,column=1)
lbl1 = tk.Label(wdw, text="Tinggi: ")
lbl1.grid(row=0,column=0)
inp2 = tk.Entry(wdw)
inp2.insert(0,'0.0')
inp2.grid(row=1,column=1)
lbl2 = tk.Label(wdw, text="Lebar: ")
lbl2.grid(row=1,column=0)

btn = tk.Button(wdw, text = "Hitung luas!", command=btn_hitung)
btn.grid(row=2,columnspan=2)
lbl3 = tk.Label(wdw, text="0.0")
lbl3.grid(row=3,columnspan=2)

wdw.mainloop()

