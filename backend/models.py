from pydantic import BaseModel, Field

class ReservaBase(BaseModel):
    laboratorio: str
    responsavel: str
    data: str
    turno: str
    finalidade: str
    quantidade_de_alunos: int = Field(..., ge=1, le=40, description="Quantidade de alunos entre 1 e 40")

class ReservaCriar(ReservaBase):
    pass

class Reserva(ReservaBase):
    id: int
    status: str
    data_criacao: str

    class Config:
        from_attributes = True