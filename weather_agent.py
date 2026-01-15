import requests

API_KEY = "b36b18dcfa37466cd78be212ad1c9d35"

print("✅ RUNNING UPDATED VERSION v2")

print("🌦️ Weather AI Agent — powered by Python")
print("Ask me about the weather in any city 🌍")



def advice(temp_c, desc):
    d = desc.lower()
    if "rain" in d or "drizzle" in d:
        return "Take an umbrella ☔"
    if "snow" in d:
        return "Wear warm layers ❄️"
    if temp_c <= 0:
        return "It’s freezing — wear a heavy jacket 🧥"
    if temp_c <= 10:
        return "It’s cold — wear a jacket 🧥"
    if temp_c >= 30:
        return "It’s hot — stay hydrated 💧"
    return "Weather looks comfortable 🙂"


def weather_agent(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return "Sorry, I couldn't find that city."

    data = response.json()

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    feels_like = data["main"]["feels_like"]

    tip = advice(temp, description)

    return (
        f"In {city}, it's {temp}°C with {description}. It feels like {feels_like}°C.\n"
        f"Agent suggestion: {tip}"
    )


user_text = input("You: ")

# allow: "weather in chicago" or just "chicago"
if " in " in user_text.lower():
    city_name = user_text.split("in", 1)[1].strip()
else:
    city_name = user_text.strip()

print(weather_agent(city_name))











