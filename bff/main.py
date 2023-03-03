from fastapi import FastAPI
import json

app = FastAPI()

with open("/workspaces/cist-cat/bff/dummy_sheet.json","r") as f:
    dummy_sheet=json.load(f)

@app.get("/")
async def root():
    return dummy_sheet