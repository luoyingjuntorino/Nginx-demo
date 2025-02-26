import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
API_KEY = "fc150d0c0823c433cdcfb87dbcf8b3b3"

class CityInput(BaseModel):
    city: str

@app.post("/weather/")
def get_weather(data: CityInput):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={data.city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    return {
        "city": data.city,
        "temperature": response["main"]["temp"],
        "humidity": response["main"]["humidity"],
        "sunrise": response["sys"]["sunrise"],
        "sunset": response["sys"]["sunset"],
        "weather": response["weather"][0]["description"]
    }
