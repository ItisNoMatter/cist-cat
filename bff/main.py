from fastapi import FastAPI
import json
import pdfManager as pdfManager
import jsonManager as jsonManager

app = FastAPI()
pdfM = pdfManager.PdfManager()
jsonM = jsonManager.JsonManager()

with open("dummy_sheet.json","r") as f:
    dummy_sheet=json.load(f)

# dummy_sheetを返す用エンドポイント
@app.get("/")
async def root():
    return dummy_sheet
 
# 本番用エンドポイント
@app.get("/getdata")
async def get_sheet():
    pdfM.get_pdf_from_web()
    print(jsonM.new_json())
    return "成功"