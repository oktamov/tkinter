from datetime import datetime
from tkinter import *
import json
import requests


def get_data():
    city = entry.get()
    key1 = 'CquPBJVd8ethk04ibQ97XOP7Kg6HLKMd'
    key2 = 'Sacxt5wjqSP4Hr8SRpmStCUO6Rp4u27H'
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={city}&apikey='Sacxt5wjqSP4Hr8SRpmStCUO6Rp4u27H"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    return json.loads(response.text)


def get_timelines():
    res = get_data()
    return res.get('timelines')


def get_daily():
    res = get_timelines()
    return res.get('daily')


def get_hourly():
    res = get_timelines()
    return res.get('hourly')


def get_minutely():
    res = get_timelines()
    return res.get('minutely')


def convert_to_datetime(date_str):
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")


def get_day_hours_temperature_with_time(day_date):
    hourly_data = get_hourly()
    data = []

    for hour_data in hourly_data:
        time = hour_data['time']
        if convert_to_datetime(time).date() == day_date.date():
            data.append({
                'time': convert_to_datetime(time).strftime("%H:%M"),
                "temperature": hour_data['values']['temperature']
            })
    return data


def get_daily_temperature():
    data = []
    for day in get_daily():
        day_values = day["values"]
        average_temperature = None
        if day_values:
            average_temperature = day_values["temperatureAvg"]
        day_date = datetime.strptime(day["time"], "%Y-%m-%dT%H:%M:%SZ")
        data.append({
            "day": day_date.strftime("%Y.%m.%d"),
            "average_temperature": average_temperature,
            "hours": get_day_hours_temperature_with_time(day_date)
        })
    return data


def window_show():
    day_lb.configure(text=get_daily_temperature()[0]['day'])
    temp_avg_txt.configure(text=get_daily_temperature()[0]['average_temperature'])
    for i in get_daily_temperature()[0]['hours']:
        if i.get('time') == "09:00":
            morning_temp.configure(text=get_daily_temperature()[0]['hours'][0].get('temperature'))
        if i.get('time') == "13:00":
            afternoon_temp.configure(text=get_daily_temperature()[0]['hours'][0].get('temperature'))
        if i.get('time') == "21:00":
            night_temp.configure(text=get_daily_temperature()[0]['hours'][0].get('temperature'))


window = Tk()
window.title("weather")
window.geometry('550x350')
window.configure(background='#000080')
entry = Entry()

select_city = Label(text="Select city>")
select_city.place(x=10, y=20)
select_city.configure(font=1, border=5, background='#FF0000')

entry.place(x=130, y=20)
entry.configure(font=1, border=4)

button = Button(text="Show", command=window_show)
button.place(x=400, y=16)
button.configure(font=1, border=5, width=7, background='#FF0000', activebackground='#660000')

day_lb = Label()
day_lb.place(x=20, y=80)
day_lb.configure(font=1, background="white", highlightbackground="green", width=10, fg='#1589FF')

temp_avg_lb = Label(text="O'rtacha harorat:")
temp_avg_lb.place(x=200, y=80)
temp_avg_lb.configure(font=1, background='#FF0000')

temp_avg_txt = Label()
temp_avg_txt.place(x=400, y=80)
temp_avg_txt.configure(font=1, background="white", width=5, fg='#1589FF')

vaqt_lb = Label(text="Vaqt:")
vaqt_lb.place(x=20, y=120)
vaqt_lb.configure(font=1, background='#FF0000')

morning_lb = Label(text="09:00")
morning_lb.place(x=110, y=120)
morning_lb.configure(font=1, background="white", width=5, fg='#FF0000')

afternoon_lb = Label(text="13:00")
afternoon_lb.place(x=180, y=120)
afternoon_lb.configure(font=1, background="white", width=5, fg='#FF0000')

night_lb = Label(text="21:00")
night_lb.place(x=250, y=120)
night_lb.configure(font=1, background="white", width=5, fg='#FF0000')

harorat_lb = Label(text="Harorat:")
harorat_lb.place(x=20, y=150)
harorat_lb.configure(font=1, background='#FF0000')

morning_temp = Label()
morning_temp.place(x=110, y=150)
morning_temp.configure(font=1, background="white", width=5, fg='#1589FF')

afternoon_temp = Label()
afternoon_temp.place(x=180, y=150)
afternoon_temp.configure(font=1, background="white", width=5, fg='#1589FF')

night_temp = Label()
night_temp.place(x=250, y=150)
night_temp.configure(font=1, background="white", width=5, fg='#1589FF')

window.mainloop()
