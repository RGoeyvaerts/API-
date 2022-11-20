from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random
import json

with open("./data.json",encoding = 'utf-8') as f:
    content = json.loads(f.read())


winner = random.choice(content)
winner = str(winner)

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


drivers=["Andreas Bakkerud","Johan Kristoffersson","Mattias Ekström","NICLAS GRÖNHOLM","Robin Larsson","OLE CHRISTIAN VEIBY","JĀNIS BAUMANIS","SONDRE EVJEN","ENZO IDE","ANTON MARKLUND","JEAN BAPTISTE DUBOURG","KOBE PAUWELS","MARIUS SOLBERG HANSEN","VIKTOR VRANCKX","ISAK SJÖKVIST","PATRICK O'DONOVAN",]
teams=["Monster Energy RX Cartel","Kristoffersson Motorsport","EKS RX","Construction Equipment Dealer Team","#YellowSquad","JC Raceteknik","EKS","SET Promotion","DA Racing","Volland Racing KFT","QEV",]


class teamIn(BaseModel):
    name:str
    team:str
    drivernumber:int

@app.get("/drivers2")
async def root():
    winner = random.choice(content)
    winner = str(winner)

    return {winner}

@app.get("/drivers")
async def root():
    return {random.choice(list(drivers))}

@app.get("/teams")
async def root():
    return {random.choice(teams)}


@app.post("/teams/", response_model=teamIn)
async def create_team(team: teamIn):
    content.append(team)
    # 3. Write json file
    with open("data.json", "w") as file:
        json.dump(content, file,default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
    return team


f.close()
