import tkinter as tk
from tkinter import messagebox

from weather_api import get_weather


# Create application window
window = tk.Tk()

window.title("Weather App")
window.geometry("400x400")
window.config(bg="white")


# Heading
title_label = tk.Label(
    window,  
    text="Weather App",
    font=("Arial", 18, "bold"),
    bg="white"
)

title_label.pack(pady=20)


# City name label
city_label = tk.Label(
    window,
    text="Enter City Name:",
    font=("Arial", 12),
    bg="white"
)

city_label.pack()


# City input box
city_entry = tk.Entry(
    window,
    width=25,
    font=("Arial", 14),
    justify="center",
    bd=3,
    relief="groove"
)

city_entry.pack(pady=10)

# Function that runs when button is clicked
def search_weather():

    city = city_entry.get()

    if city == "":
        messagebox.showwarning(
            "Input Error",
            "Please enter a city name"
        )
        return


    weather = get_weather(city)


    if weather:

        city_name, temperature, humidity = weather

        result_label.config(
            text=f"""
Weather Report

City: {city_name}

Temperature: {temperature} °C

Humidity: {humidity} %

"""
        )

    else:

        result_label.config(
            text="City not found"
        )


# Search button
search_button = tk.Button(
    window,
    text="Get Weather",
    font=("Arial", 12),
    command=search_weather
)

search_button.pack(pady=15)


# Area where result is displayed
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    bg="white"
)

result_label.pack(pady=20)


# Keep the window running
window.mainloop()