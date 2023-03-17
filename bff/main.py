from fastapi import FastAPI
import json
import pdfManager

app = FastAPI()
pdfM = pdfManager.PdfManager()

with open("dummy_sheet.json","r") as f:
    dummy_sheet=json.load(f)

@app.get("/")
async def root():
    return dummy_sheet


@app.get("/getpdf")
def get_pdf():
    pdfM.get_pdf_from_web()
        