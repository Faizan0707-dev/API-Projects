import requests

responce = requests.get("https://api.openweathermap.org/data/2.5/weather",
params = {"q" :"Kota",
          "appid":"YOUR-API-KEY",
          "units":"metric"})
data = responce.json()
print(data)
print(f"country is : {data['sys']['country']}")
print(f"city name : {data['name']}")
print(f"temp of kota is : {data['main']['temp']} °C")
print(f"whether in kota is: {data['weather'][0]['description']}")
print(f"Humidity is :{data['main']['humidity']} %")
print(f"max temp is :{data['main']['temp_max']}")
print(f"min temp is :{data['main']['temp_min']}")
print(f"Pressure is : {data['main']['pressure']}  hPa")
print(f"Wind speed is : {data['wind']['speed'] }m/s")