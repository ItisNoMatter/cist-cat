from fastapi import FastAPI
import json
app = FastAPI()

with open("dummy_sheet.json") as f:
    dummy_sheet=json.load(f)

@app.get("/")
async def root():
    return {"message": "Hello World!!"}