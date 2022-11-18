from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()
origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "https://localhost.tiangolo.com/",
    "http://127.0.0.1:5500/"
    "https://rgoeyvaerts.github.io/API-site"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)


drivers=["Andreas Bakkerud","Johan Kristoffersson","Mattias Ekström","NICLAS GRÖNHOLM","Robin Larsson","OLE CHRISTIAN VEIBY","JĀNIS BAUMANIS","SONDRE EVJEN","ENZO IDE","ANTON MARKLUND","JEAN BAPTISTE DUBOURG"]
teams=["Monster Energy RX Cartel","Kristoffersson Motorsport","EKS RX","Construction Equipment Dealer Team",]

class driverIn(BaseModel):
    username: str
class driverOut(BaseModel):
    username: str



class teamIn(BaseModel):
    username: str
class teamOut(BaseModel):
    username: str





@app.get("/drivers")
async def root():
    return {random.choice(list(drivers))}

@app.get("/teams")
async def root():
    return {random.choice(teams)}

@app.post("/drivers/", response_model=driverOut)
async def create_driver(driver: driverIn):
    return driver

@app.post("/teams/", response_model=teamOut)
async def create_team(team: teamIn):
    return team



