import tkinter as tk
import time
import requests


def getweather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=9f5ddbe67487430109c76f3b5fb3ff1d"
    json_data = requests.get(api).json()
    print(json_data)
    condition = json_data['weather'][0]['main']
    temp = (json_data['main']['temp'] - 273.15)
    min_temp = (json_data['main']['temp_min'] - 273.15)
    max_temp = (json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']))

    final_info = condition + "\n" + str(temp) + "C"
    final_data = "\n" + "MAX TEMP : " + str(max_temp) + "\n" + "MIN TEMP : " + str(
        min_temp) + "\n" + "Pressure : " + str(pressure) + "\n" + "HUMIDITY : " + str(
        humidity) + "\n" + "WIND SPEED : " + str(wind_speed) + "\n" + "SUNRISE : " + str(
        sunrise) + "\n" + "SUNSET : " + str(sunset)
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", "15", "bold")
t = ("poppins", "35", "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getweather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
