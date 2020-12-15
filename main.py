from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db.db_reservas import Reserva
from models.db_reservas_model import ReservaInfo
import datetime
from db.db_reservas import db_reserva
from db.db_reservas import get_reservas
from db.db_reservas import crear_reserva
from db.db_reservas import obtener_reservas

api = FastAPI() #comunicacion capa logica y capa presentacion

origins = [
    "http://localhost:8080"
]

api.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


@api.get("/")
async def home():
    return {"message": "Bienvenido a su Hotel MinTIC"}


@api.get("/reservas/") # retornar la DB completa
async def get_reserva():# funcion root
    reservas = obtener_reservas()
    return reservas

@api.post("/reserva/crear/")# se actualiza reserva
async def crea_reserva(rvinfo:ReservaInfo):
    createrv = crear_reserva(rvinfo)
    if createrv is True:
         return {"mensaje":"Reserva creada exitosamente"}
    else:
        raise HTTPException(
           status_code=400, detail="error, Reserva con ese id ya exisitia")
