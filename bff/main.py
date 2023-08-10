from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import json
import pdfManager as pdfManager
import jsonManager as jsonManager

app = FastAPI()
pdfM = pdfManager.PdfManager()
jsonM = jsonManager.JsonManager()

with open("dummy_sheet.json","r") as f:
    dummy_sheet=json.load(f)

# CORSを回避するために追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   
    allow_methods=["*"],      
    allow_headers=["*"]       
)

# dummy_sheetを返す用エンドポイント
@app.get("/")
async def root():
    return dummy_sheet
 
# 本番用エンドポイント
@app.get("/json")
async def get_sheet():
    # pdfM.get_pdf_from_web()
    sheet_data = jsonM.new_json()
    return sheet_data