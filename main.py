# modules
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse
from typing import Optional
import pyjokes

# app
app = FastAPI()

# configurations
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# routes

@app.get("/", response_class=HTMLResponse)
# this route renders homepage
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/joke")
# route for joke endpoint
def joke(lang: Optional[str] = "en"):
    try:
        joke = pyjokes.get_joke(language=lang)
        return {"joke": joke}
    except:
        return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)

@app.get("/jokes")
# route for jokes endpoint
def jokes(lang: Optional[str] = "en"):
    try:
        jokes = pyjokes.get_jokes(language=lang)
        return {"jokes": jokes}
    except:
        return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)