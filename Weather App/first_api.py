import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=27.7172&longitude=85.3240&current=temperature_2m"

response = requests.get(url)

print(response.status_code)

data = response.json()
temperature = data["current"]["temperature_2m"]
print("Current Temperature:", temperature, "°C")

print(data)



  