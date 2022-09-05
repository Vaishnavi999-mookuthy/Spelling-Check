import tkinter as tk
from tkinter import *
from textblob import TextBlob
from tkinter.ttk import *
from PIL import Image,ImageTk

def check_spelling():
    a=TextBlob(spell_check.get())
    rslt=str(a.correct())
    output=tk.Label(window,text="The correct spelling is : "+rslt,bg='white',font=("Ariel",18,'bold'))
    output.place(x=100,y=300)


window=tk.Tk()
window.title("Spelling Check")
window.geometry("700x1100")
window.config(background="#ffcc99")

text_head=tk.Label(window,text="Spelling AutoCorrect",font=("Times",50,"bold"),bg='white',fg='#ff8000')
text_head.place(x=40,y=30)

img=ImageTk.PhotoImage(Image.open("C:\\Users\\lenovo\\Downloads\\R.png"))
panel=Label(window,image=img)
panel.place(x=95,y=350)

text_check=tk.Label(window,text="Enter the Word",font=("Times",18),bg='white',fg='black')
text_check.place(x=100,y=150)

spell_check=tk.Entry(window,font=("Ariel",18,'bold'),width=25,bg='white',fg='black')
spell_check.place(x=280,y=150)

button=tk.Button(window,text="CHECK",command=check_spelling,font=("Times",18),fg='black',bg='#ffe6cc')
button.place(x=270,y=200)

window.mainloop()
