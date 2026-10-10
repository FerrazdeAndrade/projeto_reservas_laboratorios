from typing import List
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from models import Reserva, ReservaCriar
import services
from database import criar_tabela

app = FastAPI(
    title="Sistema de Reservas de Laboratórios",
    version="0.1.0",
    description="API para gerenciamento e agendamento de laboratórios."
)

# Configuração de CORS para requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    criar_tabela()

@app.get("/reservas", response_model=List[Reserva], summary="Listar todas as reservas")
def obter_reservas():
    return services.listar_reservas()

@app.post("/reservas", response_model=Reserva, status_code=status.HTTP_201_CREATED, summary="Criar nova reserva")
def adicionar_reserva(reserva: ReservaCriar):
    try:
        return services.criar_reserva(reserva)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))