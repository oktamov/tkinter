import csv
import os
from datetime import datetime
from tkinter_project import messagebox, END, Tk, Label, Entry, Button, Radiobutton, StringVar
from tkcalendar import DateEntry

from student import Student

students = []


def add():
    try:
        if not fullname_entry.get():
            messagebox.showinfo("Information", "You did not enter a full name!")
        elif not email_entry.get():
            messagebox.showinfo("Information", "You did not enter an email!")
        elif not dob_entry.get():
            messagebox.showinfo("Information", "You did not enter a DOB!")
        elif not gender.get():
            messagebox.showinfo("Information", "You did not enter a gender!")
        elif not phone_entry.get():
            messagebox.showinfo("Information", "You did not enter a Phone!")
        elif not dob_entry.get():
            messagebox.showinfo("Information", "You did not enter an DOB!")
        elif not course_entry.get():
            messagebox.showinfo("Information", "You did not enter an Course!")


        else:
            student = Student(
                fullname_entry.get(),
                email_entry.get(),
                dob_entry.get(),
                gender.get(),
                phone_entry.get(),
                course_entry.get(),
                datetime.now()
            )
            students.append(student.get_attrs(as_dict=True))
            messagebox.showinfo("Information", "The data has been added successfully")
    except Exception as e:
        print(e)


def save():
    with open("students.csv", "a", newline="\n") as file:
        header = ["Fullname", "Email", "DOB", "Gender", "Phone", "Course", "DOJ"]
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize("students.csv") == 0:
            csv_writer.writeheader()
        csv_writer.writerows(students)
        messagebox.showinfo("Information", "Saved successfully")


def clear():
    fullname_entry.delete(0, END)
    email_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    course_entry.delete(0, END)


def delete():
    with open("students.csv", 'w') as file:
        header = ["Fullname", "Email", "DOB", "Gender", "Phone", "Course", "DOJ"]
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

email_label = Label(text="Your email:")
email_label.place(x=10, y=50)
email_label.configure(font=1, background='#82CAFA')

email_entry = Entry()
email_entry.place(x=150, y=50)
email_entry.configure(font=1, borderwidth=5, width=30)

dob_label = Label(text="Your DOB:")
dob_label.place(x=10, y=90)
dob_label.configure(font=1, background='#82CAFA')

dob_entry = DateEntry(window)
dob_entry.place(x=150, y=90)
dob_entry.configure(font=1)

gender_label = Label(text="Your gender:")
gender_label.place(x=10, y=130)
gender_label.configure(font=1, background='#82CAFA')

gender = StringVar()
GENDER_TYPES = {"male": "Male", "female": "Female"}

male_radio_btn = Radiobutton(
    window, text=GENDER_TYPES.get("male"), value="male", variable=gender
)
male_radio_btn.place(x=150, y=130)
male_radio_btn.configure(font=1, activebackground='#2B65EC')

female_radio_btn = Radiobutton(
    window, text=GENDER_TYPES.get("female"), value="female", variable=gender
)
female_radio_btn.place(x=260, y=130)
female_radio_btn.configure(font=1, activebackground='#2B65EC')

phone_label = Label(text="Your phone:")
phone_label.place(x=10, y=170)
phone_label.configure(font=1, background='#82CAFA')

phone_entry = Entry()
phone_entry.place(x=150, y=170)
phone_entry.configure(font=1, borderwidth=5, width=30)

course_label = Label(text="Your course:")
course_label.place(x=10, y=210)
course_label.configure(font=1, background='#82CAFA')

course_entry = Entry()
course_entry.place(x=150, y=210)
course_entry.configure(font=1, borderwidth=5, width=30)

save_btn = Button(text="save", command=save)
save_btn.place(x=80, y=260)
save_btn.configure(font=1, activebackground='#2B65EC')

add_btn = Button(text="add", command=add)
add_btn.place(x=160, y=260)
add_btn.configure(font=1, width=5, activebackground='#2B65EC')

clear_btn = Button(text="clear", command=clear)
clear_btn.place(x=250, y=260)
clear_btn.configure(font=1, activebackground='#2B65EC')

exit_btn = Button(text="exit", command=window.destroy)
exit_btn.place(x=340, y=260)
exit_btn.configure(font=1, width=5, activebackground='#2B65EC')

del_btn = Button(text="delete", command=delete)
del_btn.place(x=420, y=260)
del_btn.configure(font=1, activebackground='#2B65EC')

if __name__ == "__main__":
    window.mainloop()
