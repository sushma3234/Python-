import requests

def get_weather(city):

    API_KEY = "MY_API_KEY"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if response.status_code == 200:

        city_name = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        return city_name, temperature, humidity

    else:
        return None