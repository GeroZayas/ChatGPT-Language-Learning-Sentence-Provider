from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from OpenAI_Language_Learning_Assistant import main
import pyperclip

from fastapi import FastAPI

app = FastAPI()

chat()


@app.get("/")
async def root():
    return {"message": "My name is Gero"}
