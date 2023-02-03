from pytube import YouTube
from tkinter import *



def video_download():
    text_widget.delete(1.0, END)
    text_widget.insert(END, "yuklanmoqda")

    link = link_entry.get()
    yt = YouTube(link)
    video = yt.streams.first()
    video.download(save_entry.get())

    text_widget.delete(1.0, END)
    text_widget.insert(END, f"video shu papkaga yuklandi {save_entry.get()} name: {video.title}")


window = Tk()
window.title("Age Calculator")
window.geometry("600x400")
window.configure(bg='#82CAFA')

link_label = Label(text="Video Link:")
link_label.place(x=10, y=10)
link_label.configure(font=1, background='#82CAFA')

link_entry = Entry()
link_entry.place(x=120, y=10)
link_entry.configure(font=1, width=30)

file_label = Label(text="File Path:")
file_label.place(x=10, y=40)
file_label.configure(font=1, background='#82CAFA')

save_entry = Entry()
save_entry.place(x=120, y=40)
save_entry.configure(font=1)

save_button = Button(text="Download", command=video_download)
save_button.place(x=120, y=100)
save_button.configure(font=1, background="white", activebackground="blue")

text_widget = Text(window)
text_widget.configure(state='normal')
text_widget.place(x=0, y=160)
text_widget.configure(background="white", font=20)

window.mainloop()
