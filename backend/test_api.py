import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_criar_reserva_valida():
    payload = {
        "laboratorio": "Lab 01",
        "responsavel": "Prof. Carlos",
        "data": "2026-10-15",
        "turno": "Manhã",
        "finalidade": "Aula Prática de Química",
        "quantidade_de_alunos": 25
    }
    response = client.post("/reservas", json=payload)
    assert response.status_code == 201
    dados = response.json()
    assert dados["quantidade_de_alunos"] == 25
    assert "id" in dados

def test_quantidade_alunos_invalida_zero():
    payload = {
        "laboratorio": "Lab 02",
        "responsavel": "Prof. Ana",
        "data": "2026-10-16",
        "turno": "Tarde",
        "finalidade": "Física",
        "quantidade_de_alunos": 0
    }
    response = client.post("/reservas", json=payload)
    assert response.status_code == 422  # HTTP 422 (Validação do Pydantic)

def test_quantidade_alunos_invalida_acima_do_limite():
    payload = {
        "laboratorio": "Lab 02",
        "responsavel": "Prof. Ana",
        "data": "2026-10-16",
        "turno": "Tarde",
        "finalidade": "Física",
        "quantidade_de_alunos": 45
    }
    response = client.post("/reservas", json=payload)
    assert response.status_code == 422