from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import importlib

# Import the router from our new debt app
# We use importlib to load the module because its name contains a hyphen
debt_router_module = importlib.import_module("debt-app.router")
root_router = debt_router_module.root_router
debt_router = debt_router_module.debt_router

# 1. Create the FastAPI application instance
app = FastAPI(
    title="Gbure's Budgeting App",
    description="An application for personal budget management and debt mitigation.",
    version="0.1.0",
)

# Mount the router from the debt app
app.include_router(root_router) # Handles the homepage
app.include_router(debt_router) # Handles all /debt/... routes

# 5. Placeholder route for the new budget page (from index.html link)
@app.get("/budget/new", response_class=HTMLResponse)
async def new_budget_page(request: Request):
    """
    Serves the page for creating a new budget.
    NOTE: You will need to create 'budget_entry.html' for this to work.
    """
    # For now, we can return a simple message or redirect.
    # Once 'budget_entry.html' is created, change the return statement.
    # return templates.TemplateResponse("budget_entry.html", {"request": request})
    return HTMLResponse(content="""
        <h1>Create New Budget Page</h1>
        <p>This page is under construction. The 'budget_entry.html' template needs to be created.</p>
        <a href="/">Go back home</a>
    """)
