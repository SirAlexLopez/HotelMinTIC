from fastapi import FastAPI
from fastapi import HTTPException
from db.db_reservas import Reserva
from models.db_reservas_model import ReservaInfo
import datetime
from db.db_reservas import db_reserva

app = FastAPI() #comunicacion capa logica y capa presentacion


@app.get("/") # retornar mensaje
async def root():
    return {"message": "Bienvenidos Hotel Mintic"}

@app.get("/reserva/") # retornar la DB completa
async def reserva():# funcion root
    return {"message": db_reserva}

@app.get("/reserva/{id}")# GET reserva por ID
async def get_reserva_by_id(id : int):# funcion reserva
    if id in db_reserva:
        return {"message": db_reserva[id]}
    raise HTTPException(status_code = 404, detail="La reserva no existe!")

@app.post("/reserva/")# se actualiza reserva
async def crear_reserva(rvinfo : ReservaInfo):
    db_reserva[rvinfo.id]= rvinfo
    return rvinfo

@app.delete("/reserva/")
async def eliminar_reserva(rvinfo : ReservaInfo):
    del db_reserva[rvinfo.id]
    return rvinfo

@app.put("/reserva/")
async def crear_reserva(rvinfo : ReservaInfo):
    db_reserva[rvinfo.id]= rvinfo
    return rvinfo
