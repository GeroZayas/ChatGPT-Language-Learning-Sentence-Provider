from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from OpenAI_Language_Learning_Assistant import main as chat_main
import pyperclip


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    chat_main("")
    return {"message": "My name is Gero"}
