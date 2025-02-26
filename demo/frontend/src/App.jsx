import { useState } from 'react'
import './App.css'

function App() {
  const [city, setCity] = useState('')
  const [weather, setWeather] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    const response = await fetch('/api/weather/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ city: city }),
    })
    const data = await response.json()
    setWeather(data)
  }

  return (
    <>
      <div>
        <h1>天气查询</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={city}
            onChange={(e) => setCity(e.target.value)}
            placeholder="输入城市"
          />
          <button type="submit">查询</button>
        </form>
        {weather && (
          <div style={{ marginTop: "20px" }}>
            <h2>{weather.city} 的天气</h2>
            <p>🌡 温度: {weather.temperature}°C</p>
            <p>💧 湿度: {weather.humidity}%</p>
            <p>🌅 日出时间: {new Date(weather.sunrise * 1000).toLocaleTimeString()}</p>
            <p>🌇 日落时间: {new Date(weather.sunset * 1000).toLocaleTimeString()}</p>
            <p>☁ 天气: {weather.weather}</p>
          </div>
        )}

      </div>
    </>
  )
}

export default App
