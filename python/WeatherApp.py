import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Sign up for an API key from OpenWeatherMap or similar
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
    else:
        print("City not found!")

# Example usage
city = input("Enter city name: ")
get_weather(city)
