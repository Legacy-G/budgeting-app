from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from jinja2 import ChoiceLoader, FileSystemLoader

from .models import DebtProfileCreate

# Create a router for the root path (homepage)
root_router = APIRouter()

# Create a separate, prefixed router for all debt-related endpoints
debt_router = APIRouter(
    prefix="/debt",
    tags=["debt"]
)

# This router needs its own template directory
# We create a loader that checks the app's template folder first, then the root one.
templates = Jinja2Templates(
    directory="debt-app/templates",
    loader=ChoiceLoader([
        FileSystemLoader("debt-app/templates"),
        FileSystemLoader("templates"),
    ])
)

@debt_router.get("/hub", response_class=HTMLResponse)
async def debt_hub_page(request: Request):
    """
    Serves the main navigation hub for the debt feature.
    """
    return templates.TemplateResponse("debt_hub.html", {"request": request})

@root_router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serves the main landing page (index.html) from the debt app's templates.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@debt_router.get("/new", response_class=HTMLResponse)
async def new_debt_profile_page(request: Request):
    """
    Serves the page to create a new debt profile.
    """
    return templates.TemplateResponse("debt_calculator.html", {"request": request})

@debt_router.get("/profiles", response_class=HTMLResponse)
async def debt_profiles_page(request: Request):
    """
    Serves the page that lists all existing debt profiles.
    """
    return HTMLResponse(content="<h1>Debt Profiles Page (Under Construction)</h1><a href='/debt/hub'>Back to Hub</a>")

@debt_router.post("/api/profiles", status_code=201)
async def create_debt_profile(profile: DebtProfileCreate):
    """
    API endpoint to receive and save a new debt profile.
    """
    print("--- New Debt Profile Received ---")
    print(profile.model_dump_json(indent=2))
    return {"message": "Debt profile created successfully", "data": profile}