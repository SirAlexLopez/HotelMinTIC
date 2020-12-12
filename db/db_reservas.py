from pydantic import BaseModel
from datetime import date
from typing import  Dict

class Reserva(BaseModel): #definir parametros
    id: int
    quien_reserva: str
    fecha_entrada: date
    fecha_salida: date
    numero_noches: int
    tipo_habitacion: str
    numero_personas: int
    numero_habitacion: int
    precio: int

db_reserva = Dict[str, Reserva]#creamos el diccionario

db_reserva = {#base de datos
    1: Reserva(**{"id":1,
                    "quien_reserva" : "Juan Peréz", 
                    "fecha_entrada": "2020-12-13", 
                    "fecha_salida":"2020-12-18", 
                    "numero_noches": 5, 
                    "tipo_habitacion":"Doble", 
                    "numero_personas":2, 
                    "numero_habitacion":305, 
                    "precio":690000}),
    2: Reserva(**{"id":2,
                    "quien_reserva" : "Mario Gomez", 
                    "fecha_entrada": "2020-12-20", 
                    "fecha_salida":"2020-01-06", 
                    "numero_noches": 17, 
                    "tipo_habitacion":"Sencilla", 
                    "numero_personas":1, 
                    "numero_habitacion":108, 
                    "precio":1750000}),
    3: Reserva(**{"id":3, 
                    "quien_reserva": "Camila Reyes", 
                    "fecha_entrada": "2021-01-03", 
                    "fecha_salida":"2021-01-23", 
                    "numero_noches": 20, 
                    "tipo_habitacion":"Suit", 
                    "numero_personas":2, 
                    "numero_habitacion":501, 
                    "precio":3100000})
}

def get_reservas (id:int):# obteniendo con GET un objeto
    if id in db_reserva.keys():
        return db_reserva[id]
    else:
        return None

def update_reserva(reserva:Reserva):# actualizamos con PUT el objeto
    db_reserva[reserva.id] = reserva
    return reserva





