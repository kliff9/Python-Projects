from tkinter import *


window = Tk()
window.title("Miles to KM")
window.minsize(width=500, height=500)

label = Label(text="Convert")
label.pack()


entry = Entry(width=30)
entry.pack()

def calc():

    new_value2 = float(entry.get()) * 1.609344
    label.config(text=round(new_value2))

button = Button(text="calculate", command=calc)
button.pack()


window.mainloop()