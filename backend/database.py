import sqlite3
from pathlib import Path

# Aponta o caminho para salvar na pasta 'dados/reservas.db'
DB_DIR = Path(__file__).resolve().parent.parent / "dados"
DB_PATH = DB_DIR / "reservas.db"

def conectar():
    # Garante que a pasta 'dados' existe antes de conectar
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela():
    with conectar() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            laboratorio TEXT NOT NULL,
            responsavel TEXT NOT NULL,
            data TEXT NOT NULL,
            turno TEXT NOT NULL,
            finalidade TEXT NOT NULL,
            quantidade_de_alunos INTEGER NOT NULL,
            status TEXT NOT NULL,
            data_criacao TEXT NOT NULL
        )
        """)