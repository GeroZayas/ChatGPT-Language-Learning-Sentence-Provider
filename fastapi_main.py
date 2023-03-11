from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from OpenAI_Language_Learning_Assistant import main as chat_main
import pyperclip


from fastapi import FastAPI


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

the_response = chat_main(
    language="Spanish",
    prompt="La vida",
    type_generation="Questions",
    num_phrases=5,
    loop="no",
)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request, response=the_response):
    return templates.TemplateResponse(
        "index.html", {"request": request, "response": response}
    )
