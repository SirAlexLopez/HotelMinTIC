from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.db_reservas_model import ReservaInfo
from db.db_reservas import Reserva,db_reserva,get_reservas,crear_reserva,obtener_reservas,eliminar_reserva
import datetime

api = FastAPI() #comunicacion capa logica y capa presentacion

origins = [
    "http://localhost:8080",
    "https://hotelmintic-app.herokuapp.com"
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

@api.delete("/reserva/borrar/")
async def delete_reserva(rvinfo:ReservaInfo):
    deleterv = eliminar_reserva(rvinfo)
    if deleterv is True:
        return {"mensaje":"Reserva borrada exitosamente"}
    else:
        raise HTTPException(
           status_code=400, detail="error, Reserva con ese id no existe")