from fastapi import FastAPI
import json
import requests

app = FastAPI()

def get_sheet():
    r=requests.get("timetable-parser")
    return r

with open("dummy_sheet.json","r") as f:
    dummy_sheet=json.load(f)

@app.get("/")
async def root():
    return dummy_sheet