import requests
from fastapi import FastAPI, APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os

API_KEY = os.environ["API_KEY"]  # 从环境变量中获取 API_KEY

version = "1.3"
app = FastAPI()
router = APIRouter(prefix="/api/weather/v1")

# API_KEY = "fc150d0c0823c433cdcfb87dbcf8b3b3"

# 👇允许本地 React 前端访问的设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://web.yingjuntorino.xyz"],  # 指定允许来源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CityInput(BaseModel):
    city: str

@router.get("/info")
async def get_info():
    return {
        "name": "FastAPI Weather Service",
        "version": version,
        "description": "A service to fetch weather information for a given city.",
        "timestamp": datetime.now().isoformat(),
    }

@router.get("/weather")
def get_weather(city: str = Query(..., description="City name to get weather for")):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return JSONResponse(
                status_code=r.status_code,
                content={"error": f"Failed to fetch weather data: {r.json().get('message', 'Unknown error')}"}
            )

        response = r.json()

        return {
            "city": city,
            "temperature": response["main"]["temp"],
            "humidity": response["main"]["humidity"],
            "sunrise": response["sys"]["sunrise"],
            "sunset": response["sys"]["sunset"],
            "weather": response["weather"][0]["description"]
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Server error occurred: {str(e)}"}
        )

app.include_router(router)