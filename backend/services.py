from datetime import datetime
from database import conectar
from models import ReservaCriar

def listar_reservas():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservas ORDER BY id DESC")
        return [dict(row) for row in cursor.fetchall()]

def criar_reserva(reserva: ReservaCriar):
    with conectar() as conn:
        cursor = conn.cursor()
        
        # Verificação de conflito (mesmo laboratório, data e turno)
        cursor.execute(
            "SELECT id FROM reservas WHERE laboratorio = ? AND data = ? AND turno = ?",
            (reserva.laboratorio, reserva.data, reserva.turno)
        )
        if cursor.fetchone():
            raise ValueError("Já existe uma reserva para este laboratório no mesmo dia e turno.")

        data_criacao = datetime.now().isoformat()
        status = "CONFIRMADA"

        cursor.execute(
            """
            INSERT INTO reservas (laboratorio, responsavel, data, turno, finalidade, quantidade_de_alunos, status, data_criacao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                reserva.laboratorio,
                reserva.responsavel,
                reserva.data,
                reserva.turno,
                reserva.finalidade,
                reserva.quantidade_de_alunos,
                status,
                data_criacao
            )
        )
        conn.commit()
        
        reserva_id = cursor.lastrowid
        cursor.execute("SELECT * FROM reservas WHERE id = ?", (reserva_id,))
        return dict(cursor.fetchone())