from fastapi import FastAPI
import json
import pdfManager
import requests

app = FastAPI()
pdfM = pdfManager.PdfManager()

def get_sheet():
    r=requests.get("/")
    return r

with open("dummy_sheet.json","r") as f:
    dummy_sheet=json.load(f)

@app.get("/")
async def root():
    return dummy_sheet


@app.get("/getpdf")
def get_pdf():
    pdfM.get_pdf_from_web()
        