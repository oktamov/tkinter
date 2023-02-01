import speech_recognition as sr
from tkinter_project import *
from gtts import gTTS
import os
from googletrans import Translator

r = sr.Recognizer()


def recognition():
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("gapir...")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        text_widget.delete(1.0, END)
        text_widget.insert(END, text)


#
# def speech_trans():
#     text = "Hello World"
#     translator = Translator()
#     translation = translator.translate(text, src='es', dest='en').text
#     print(translation)
#     text_widget.delete(1.0, END)
#     text_widget.insert(END, translation)





window = Tk()
window.title("Registration")
window.geometry("600x400")
window.configure(bg='#82CAFA')



add_btn = Button(text="gapir", command=recognition)
add_btn.place(x=120, y=100)
add_btn.configure(font=1, width=5, activebackground='#2B65EC')


text_widget = Text(window)
text_widget.configure(state='normal')
text_widget.place(x=0, y=160)
text_widget.configure(background="white", font=20)

window.mainloop()















#
#
#
#
# # text = "шрум"
# # language = "ru"
# #
# # tts = gTTS(text=text, lang=language, slow=False)
# #
# # tts.save("hello_uz.mp3")
# #
# # os.system("hello_uz.mp3")

# print(recognition())
#
#
# from googletrans import Translator
#
# # Initialize the translator
# translator = Translator(service_urls=['translate.google.com'])
#
# # Translate the text
# text_to_translate = "Hello, how are you?"
# translated_text = translator.translate(text_to_translate, dest='ru').text
#
# print(translated_text)