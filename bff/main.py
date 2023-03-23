from fastapi import FastAPI
import json
# import requests

app = FastAPI()

# 本番用
def get_sheet():
    r=requests.get("/")
    return r

with open("dummy_sheet.json","r") as f:
    dummy_sheet=json.load(f)

# dummy_sheetを返す用
@app.get("/")
async def root():
    return dummy_sheet
        