import tkinter as tk
from tkinter import ttk, messagebox
import requests

from country_currency import country


def get_exchange_rate():
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{combo1.get()}"
        response = requests.get(url)
        data = response.json()
        result = data['rates'][combo2.get()]
        result = float(result) * float(entry1.get(1.0, tk.END))

        entry2.delete(1.0, tk.END)
        entry2.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Error", "\nNoto'gri kiritdingiz")


root = tk.Tk()
root.geometry("650x450")
root.configure(background='#2B65EC')

combo1 = ttk.Combobox(root, font="Arial 15", width=15, background='white')
combo1['values'] = list(country.keys())
combo1.current(0)
combo1.place(x=10, y=10)

entry1 = tk.Text(font=1, border=3, width=20, background='#82CAFA')
entry1.place(x=5, y=70)

combo2 = ttk.Combobox(root, font="Arial 15", width=15)
combo2['values'] = list(country.keys())
combo2.current(0)
combo2.place(x=450, y=10)

convert_btn = tk.Button(text="<Exange>", font=1, border=4, activebackground="blue", background='white',
                        command=get_exchange_rate)
convert_btn.place(x=270, y=30)

entry2 = tk.Text(font=1, border=3, width=20, background='#82CAFA')
entry2.place(x=420, y=70)

root.mainloop()
