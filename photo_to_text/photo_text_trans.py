import tkinter as tk
from tkinter import messagebox, filedialog

import pytesseract
from PIL import Image
from translate import Translator


file_path = " "

def open_image():
    global file_path

    del file_path
    file = filedialog.askopenfilename(initialdir="D:/")
    file_path = file
def extract_text():
    try:
        image_path = file_path

        image = Image.open(image_path)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

        text = pytesseract.image_to_string(image)

        text_widget.configure(state='normal')
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, text)
        text_widget.configure(state='disabled')
    except Exception as e:
        messagebox.showerror("Error", "Error: file path not found")

def trans_text():
    try:
        image_path = file_path

        image = Image.open(image_path)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

        text = pytesseract.image_to_string(image)


        translator = Translator(to_lang="uz")
        translation = translator.translate(text)
        text_widget.configure(state='normal')
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, translation)
        text_widget.configure(state='disabled')
    except Exception:
        messagebox.showerror("Error", "Error: file path not found")


if __name__ == "__main__":

    gui = tk.Tk()
    gui.title("Image to Text")
    gui.geometry('600x500')
    gui.configure(bg='#82CAFA')


    file_btn=tk.Button(text="Open", border=4, command=open_image)
    file_btn.pack()
    file_btn.configure(font=1, activebackground="blue", background="white")

    label = tk.Label(text="open image 👆")
    label.pack()
    label.configure(font=1, bg='#82CAFA')

    extract_button = tk.Button(gui, text="Extract Text", command=extract_text)
    extract_button.pack()
    extract_button.configure(font=1, activebackground="blue", background="white")

    trans_button = tk.Button(gui, text="Translate to uzb", command=trans_text)
    trans_button.pack()
    trans_button.configure(font=1, activebackground="blue", background="white")

    text_widget = tk.Text(gui)
    text_widget.pack()
    text_widget.configure(state='disabled')


    gui.mainloop()
