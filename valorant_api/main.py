import logging
import os
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from valorant_api.Val import valorant


logs_file = Path(Path().resolve(), "log.txt")
logs_file.touch(exist_ok=True)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=os.environ.get("LOGLEVEL", "INFO"),
    handlers=[logging.FileHandler(logs_file), logging.StreamHandler()],
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
    if news_data == []:
        return templates.TemplateResponse(
        "nothing.html",{"request": request }

    )
    else:
        return templates.TemplateResponse(
            "news.html",{"request": request, "news_data" : news_data,   }

        )

@app.get("/rankings", response_class=HTMLResponse)
async def ranks(request: Request):
    data = valorant.get_rankings()
    return templates.TemplateResponse(
        "rankings.html", {"request": request, "ranking_data": data}
    )

@app.get("/rankings/{region}", response_class=HTMLResponse)
async def regions(request: Request, region : str):
    data = valorant.get_region_rank(region)
    return templates.TemplateResponse(
        "region.html", {"request": request, "data": data}
    )


@app.get("/login", response_class=HTMLResponse)
async def regions(request: Request):

    return templates.TemplateResponse(
        "login.html", {"request": request, }
    )

@app.get("/sign_up", response_class=HTMLResponse)
async def regions(request: Request):

    return templates.TemplateResponse(
        "sign_up.html", {"request": request, }
    )
