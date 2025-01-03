import uvicorn
from fastapi import FastAPI
from src import routes
from src.authentication import generate_jwt

app = FastAPI()
app.include_router(routes.router)

@app.get("/token")
async def get_token():
    return {"token": generate_jwt()}
