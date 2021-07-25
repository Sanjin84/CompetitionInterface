from tkinter import *
import random, time
import requests
#import wikipedia

root = Tk()
root.geometry('400x400')

tic = 0.0

def get_weather():
    city = city_entry.get()
    api_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': '11c0d3dc6093f7442898ee49d2430d20',
        'units': 'metric'
        }
    response = requests.get(api_url, params=params)
    data = response.json()
    weather = data["name"]  + " " + data["sys"]["country"] + '\n'\
    "temp: " + str(data["main"]["temp"]) + '\n' +\
     "humidity: " + str(data["main"]["humidity"]) + '\n' +\
     "clouds:" + str(data["clouds"])


    result_label.config(text = weather)

    #turn button greeen after 1 - 3 seconds

img = PhotoImage(file="landscape.png")
# Result label
# Start test button
background_image=PhotoImage(file="landscape.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = background_image


frame = Frame(root, bg="red")

#City Entry
city_entry = Entry(frame, text = 'ENTER CITY NAME')

result_label = Label(frame, text="WEATHER APP", bg="light blue")
begin_button = Button(frame, text="GET WEATHER",
                activebackground="grey",
                command = lambda: get_weather())

city_entry.place(relx=0, rely=0, relwidth=1, relheight=0.15)
begin_button.place(relx=0, rely=0.15, relwidth=1, relheight=0.15)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
result_label.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)


root.mainloop()
