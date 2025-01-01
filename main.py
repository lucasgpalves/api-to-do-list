import uvicorn
from fastapi import FastAPI
from src import ConnectionDB, routes

conn = ConnectionDB.init_connection()

app = FastAPI()
app.include_router(routes.router)
