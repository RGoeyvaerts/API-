from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random
import json

with open("app/data.json",encoding = 'utf-8') as f:
    content = json.loads(f.read())






l={1:{"drivernumber":13,"name":"Andreas Bakkerud","team":"Monster Energy RX Cartel"},2:{"drivernumber":4,"name":"Robin Larsson","team":"Monster Energy RX Cartel"},3:{"drivernumber":1,"name":"Johan Kristoffersson","team":"Kristoffersson Motorsport"},4:{"drivernumber":1,"name":"Mattias Ekström","team":"EKS RX"},5:{"drivernumber":68,"name":"Niclas Gronhölm","team":"Construction Equipment Dealer Team"},6:{"drivernumber":52,"name":"OLE CHRISTIAN VEIBY","team":"Kristoffersson Motorsport"},7:{"drivernumber":6,"name":"JĀNIS BAUMANIS","team":"#YellowSquad"},8:{"drivernumber":69,"name":"Sondre Evjen","team":"JC Raceteknik"},9:{"drivernumber":91,"name":"JĀNIS BAUMANIS","team":"#YellowSquad"},7:{"drivernumber":6,"name":"Enzo Ide","team":"EKS"}}







app = FastAPI()


origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "https://localhost.tiangolo.com/",
    "http://127.0.0.1:5500/",
    "https://rgoeyvaerts.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



drivers=["Andreas Bakkerud","Johan Kristoffersson","Mattias Ekström","NICLAS GRÖNHOLM","Robin Larsson","OLE CHRISTIAN VEIBY","JĀNIS BAUMANIS","SONDRE EVJEN","ENZO IDE","ANTON MARKLUND","JEAN BAPTISTE DUBOURG","KOBE PAUWELS","MARIUS SOLBERG HANSEN","VIKTOR VRANCKX","ISAK SJÖKVIST","PATRICK O'DONOVAN"]



class teamIn(BaseModel):
    name:str
    team:str
    drivernumber:int

@app.get("/drivers2")
async def root():
  return str(l[random.randrange(1,len(l),1)])


@app.get("/drivers")
async def root():
    return {random.choice(list(drivers))}



@app.post("/teams/", response_model=teamIn)
async def create_team(team: teamIn):
    l[len(l)+1]=team
    print(l)
    return team



