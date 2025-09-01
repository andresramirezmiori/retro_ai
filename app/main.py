from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import websockets
from app.database import Base, engine
from app import models  # esto asegura que se importen todos los modelos


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Este bloque se ejecuta al iniciar la app
    Base.metadata.create_all(bind=engine)
    yield
    # Este bloque se ejecuta al cerrar la app (si querés cleanup)


app = FastAPI(lifespan=lifespan)

app.include_router(websockets.router)

@app.get("/")
def read_root():
    return {"message": "Hola desde RetroIA"}
