from tkinter import *


def calc_age():
    year = int(dob_entry.get())
    age = 2023 - year
    text_widget.delete(1.0, END)
    text_widget.insert(END, f'yoshingiz: {age} da')


window = Tk()
window.title("Age Calculator")
window.geometry("600x400")
window.configure(bg='#82CAFA')

year_label = Label(text="Birthday:")
year_label.place(x=10, y=10)
year_label.configure(font=1, background='#82CAFA')

dob_entry = Entry()
dob_entry.place(x=100, y=10)
dob_entry.configure(font=1)

calc_button = Button(text="calculate", command=calc_age)
calc_button.place(x=80, y=60)
calc_button.configure(font=1)

text_widget = Text(window)
text_widget.configure(state='normal')
text_widget.place(x=0, y=160)
text_widget.configure(background="white", font=20)

window.mainloop()
