from fastapi import FastAPI
from fastapi import HTTPException
from db.db_reservas import Reserva
from models.db_reservas_model import ReservaInfo
import datetime
from db.db_reservas import db_reserva
from db.db_reservas import get_reservas
from db.db_reservas import crear_reserva

app = FastAPI() #comunicacion capa logica y capa presentacion

@app.get("/reserva/") # retornar la DB completa
async def reserva():# funcion root
    return {"message": db_reserva}

@app.post("/reserva/crear/{id}")# se actualiza reserva
async def crea_reserva(id: str, reserve:Reserva):
    createrv = crear_reserva(reserve)
    if createrv:
         return {"mensaje":"Reserva creada exitosamente"}
    else:
        raise HTTPException(
           status_code=400, detail="error, Reserva con ese id ya exisitia")
