import speech_recognition as sr
from tkinter import *
from translate import Translator

r = sr.Recognizer()

word = [" "]


def recognition():
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("gapir...")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        del word[0]
        word.append(text)


def speech_trans():
    translator = Translator(to_lang="uz")
    translation = translator.translate(word[0])
    text_widget.delete(1.0, END)
    text_widget.insert(END, translation)


window = Tk()
window.title("Registration")
window.geometry("600x400")
window.configure(bg='#82CAFA')

add_btn = Button(text="gapir", command=recognition)
add_btn.place(x=120, y=100)
add_btn.configure(font=1, width=5, activebackground='#2B65EC')

result_btn = Button(text='natija', command=speech_trans)
result_btn.place(x=210, y=100)
result_btn.configure(font=1, width=5, activebackground='#2B65EC')

text_widget = Text(window)
text_widget.configure(state='normal')
text_widget.place(x=0, y=160)
text_widget.configure(background="white", font=20)

window.mainloop()
