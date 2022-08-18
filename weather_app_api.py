from tkinter import *
import requests
import json

root = Tk()
root.geometry("400x400")
root.title("Weather")
city = StringVar()



def information():
    api_key = "847dd752a2324a12970134042220407"
    city_inf = city.get()
    weather_url = "http://api.weatherapi.com/v1/current.json?key=" + api_key + "&q=" + city_inf + "&aqi=no"
    response = requests.get(weather_url)
    weather_inf = response.json()

    if response.status_code == requests.codes.ok:
        date = weather_inf['location']['localtime']
        weather_a = weather_inf['current']['condition']['text']
        if weather_inf['current']['is_day'] == 1:
            day = 'It is day'
        else:
            day = 'It is night'
        temp = weather_inf['current']['temp_c']
        weather = f"\nWeather of: {city_inf}\nTemperature: {temp}°\nAbout day: {day}\nDate: {date}\nMore information about weather: {weather_a}"
    else:
        weather = "Error"
    text_field.delete('1.0','end')
    text_field.insert(INSERT,weather)
    # print(weather)

city_head = Label(root, text="Enter a city:").pack()
input_city = Entry(root, textvariable=city, width=24).pack()
btn = Button(root, text="Check weather", command=information).pack()
weather_now = Label(root, text="The weather is:").pack(pady=20)
text_field = Text(root, width=70, height=20)
text_field.pack()
# print(information())
root.mainloop()

