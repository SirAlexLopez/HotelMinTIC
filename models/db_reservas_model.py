from pydantic import BaseModel
from datetime import date

class ReservaInfo(BaseModel):
    id: int
    quien_reserva: str
    fecha_entrada: date
    fecha_salida: date
    numero_noches: int
    tipo_habitacion: str
    numero_personas: int
    precio: int

