import logging
import os
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from valorant_api.Val import valorant



logging.basicConfig(
    filename="log.txt", level=logging.INFO
)

log = logging.getLogger(__name__)


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

valorant = valorant()

@app.get("/",response_class=HTMLResponse)
async def root(request : Request):

    return templates.TemplateResponse(
        "base.html", {"request": request}

    )

@app.get("/news", response_class=HTMLResponse)
async def news(request: Request, keywords: str = ""):
    news_data = valorant.get_news(keywords = keywords )
    log.info(keywords)
    if news_data == []:
        return templates.TemplateResponse(
        "nothing.html",{"request": request }

    )
    else:
        return templates.TemplateResponse(
            "news.html",{"request": request, "news_data" : news_data,   }

        )



