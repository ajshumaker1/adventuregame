from tkinter import *
import time

root = Tk()
root.title('Adventure Game')
#root.geometry('1200x600')
root.configure(background='black')

def changeMessage():
    w2.config(text='Something new')
    Tk.update()

logo = PhotoImage(file="images/guy.jpg")
#logo = PhotoImage(file="images/space_man.gif")
#w1 = Label(root, image=logo).pack(side="right")
#explanation = """At present, only GIF and PPM/PGM
#formats are supported, but an interface 
#exists to allow additional image file
#formats to be added easily."""
#w2 = Label(root, 
#           compound=CENTER,
#           #padx = 10, 
#           text=explanation,
#           image=logo).pack(side="right")

w1 = Label(root, image=logo,
      compound=CENTER,
      bg='gray').grid(row=0)
w2 = Label(root,
      text='You are Waffle Waffleman.',
		 fg = 'white',
                 bg = 'black',
		 font = 'Verdana 10 bold',
      ).grid(row=1).pack()

root.after(5000, changeMessage)
root.mainloop()




