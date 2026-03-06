from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.agent import ask_database

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": None}
    )

@app.post("/ask")
def ask(request: Request, question: str = Form(...)):

    result = ask_database(question)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result,
            "question": question
        }
    )