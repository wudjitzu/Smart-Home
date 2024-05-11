from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()

# Przykładowa baza danych symulująca odczyty z czujników
sensor_data = {
    "temperature": 25.0,
    "humidity": 50.0,
    "pressure": 1013.25
}

# Klasa modelu dla zmiany temperatury i wilgotności
class SensorUpdate(BaseModel):
    temperature: int
    humidity: int

# Endpoint do pobierania danych z czujników
@app.get("/sensor-data")
async def read_sensor_data():
    return sensor_data

# Endpoint do aktualizacji danych z czujników (temperatury i wilgotności)
@app.post("/sensor-data")
async def update_sensor_data(sensor_update: SensorUpdate):
    sensor_data.update(sensor_update.dict())
    return sensor_data

# Endpoint do aktualizacji tylko temperatury
@app.patch("/sensor-data/temperature")
async def update_temperature(temperature: float):
    sensor_data["temperature"] = temperature
    return sensor_data

# Endpoint do aktualizacji tylko wilgotności
@app.patch("/sensor-data/humidity")
async def update_humidity(humidity: float):
    sensor_data["humidity"] = humidity
    return sensor_data
