import csv
import os
from tkinter import messagebox, END, Tk, Label, Entry, Button
from datetime import datetime

from person import Person

persons = []
grades ={}


def calc():
    if not date_entry.get():
        messagebox.showinfo("Information", "you did not entry the date!")

    if not age_entry.get():
        messagebox.showinfo("Information", "you did not entry the date!")

    else:
        if int(age_entry.get()) <= 18:
            age_entry.delete(0, END)
            messagebox.showinfo("Information", "Registration is not permitted for persons under 18 years of age")

        grade = 100 * int(date_entry.get())
        grade_label_calc.configure(text=f'{grade} $')
        grades.update({"Grade": f"{grade} $"})




def add():

    try:
        if not fullname_entry.get():
            messagebox.showinfo("Information", "You did not enter a full name!")
        elif not age_entry.get():
            messagebox.showinfo("Information", "You did not enter an email!")
        elif not locatsion_entry.get():
            messagebox.showinfo("Information", "You did not enter a DOB!")
        elif not date_entry.get():
            messagebox.showinfo("Information", "You did not enter a gender!")


        else:
            person = Person(
                fullname_entry.get(),
                age_entry.get(),
                locatsion_entry.get(),
                date_entry.get(),
                grades.get("Grade"),
                datetime.now()
            )
            persons.append(person.get_attrs(as_dict=True))
            messagebox.showinfo("Information", "The data has been added successfully")



    except Exception as e:
        print(e)


def save():
    with open("registration.csv", "a", newline="\n") as file:
        header = ["Fullname", "Age", "Locatsion", "Date", "Grade", "DOJ"]
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize("registration.csv") == 0:
            csv_writer.writeheader()
        csv_writer.writerows(persons)

        messagebox.showinfo("Information", "Saved successfully")


def clear():
    fullname_entry.delete(0, END)
    age_entry.delete(0, END)
    locatsion_entry.delete(0, END)
    date_entry.delete(0, END)
    grade_label_calc.configure(text="")


def delete():
    with open("registration.csv", 'w') as file:
        header = ["Fullname", "Age", "Address", "Date"]
        writer = csv.DictWriter(file, header)
        writer.writeheader()


window = Tk()
window.title("Registration")
window.geometry("600x400")
window.configure(bg='#82CAFA')

fullname_label = Label(text="Your name:")
fullname_label.place(x=10, y=10)
fullname_label.configure(font=1, background='#82CAFA')

fullname_entry = Entry()
fullname_entry.place(x=150, y=10)
fullname_entry.configure(font=1, borderwidth=5, width=30)

age_label = Label(text="Your age:")
age_label.place(x=10, y=50)
age_label.configure(font=1, background='#82CAFA')

age_entry = Entry()
age_entry.place(x=150, y=50)
age_entry.configure(font=1, borderwidth=5, width=30)

locatsion_label = Label(text="Your address:")

locatsion_label.place(x=10, y=90)
locatsion_label.configure(font=1, background='#82CAFA')

locatsion_entry = Entry()
locatsion_entry.place(x=150, y=90)
locatsion_entry.configure(font=1, borderwidth=5, width=30)

date_label = Label(text="date (day):")
date_label.place(x=10, y=130)
date_label.configure(font=1, background='#82CAFA')

date_entry = Entry()
date_entry.place(x=150, y=130)
date_entry.configure(font=1, borderwidth=5, width=30)

grade_label = Label(text="grade:")
grade_label.place(x=10, y=170)
grade_label.configure(font=1, background='#82CAFA')

grade_label_calc = Label()
grade_label_calc.place(x=150, y=170)
grade_label_calc.configure(font=1, borderwidth=5, width=30)

save_btn = Button(text="save", command=save)
save_btn.place(x=60, y=220)
save_btn.configure(font=1, activebackground='#2B65EC')

calc_btn = Button(text="calc", command=calc)
calc_btn.place(x=130, y=220)
calc_btn.configure(font=1, width=5, activebackground='#2B65EC')

add_btn = Button(text="add", command=add)
add_btn.place(x=210, y=220)
add_btn.configure(font=1, width=5, activebackground='#2B65EC')

clear_btn = Button(text="clear", command=clear)
clear_btn.place(x=290, y=220)
clear_btn.configure(font=1, activebackground='#2B65EC')

exit_btn = Button(text="exit", command=window.destroy)
exit_btn.place(x=370, y=220)
exit_btn.configure(font=1, width=5, activebackground='#2B65EC')

del_btn = Button(text="delete", command=delete)
del_btn.place(x=450, y=220)
del_btn.configure(font=1, activebackground='#2B65EC')

if __name__ == "__main__":
    window.mainloop()
