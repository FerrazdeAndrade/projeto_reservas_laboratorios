const API_URL = "http://127.0.0.1:8000/reservas";

document.addEventListener("DOMContentLoaded", () => {
    carregarReservas();
});

async function carregarReservas() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("Erro ao carregar reservas");
        
        const reservas = await response.json();
        const tbody = document.getElementById("tabela-reservas");
        tbody.innerHTML = "";

        reservas.forEach(reserva => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td>${reserva.id}</td>
                <td>${reserva.laboratorio}</td>
                <td>${reserva.responsavel}</td>
                <td>${reserva.data}</td>
                <td>${reserva.turno}</td>
                <td>${reserva.finalidade}</td>
                <td>${reserva.quantidade_de_alunos}</td>
                <td><strong>${reserva.status}</strong></td>
            `;
            tbody.appendChild(tr);
        });
    } catch (error) {
        console.error("Erro na requisição:", error);
    }
}

document.getElementById("form-reserva").addEventListener("submit", async (e) => {
    e.preventDefault();

    const dados = {
        laboratorio: document.getElementById("laboratorio").value,
        responsavel: document.getElementById("responsavel").value,
        data: document.getElementById("data").value,
        turno: document.getElementById("turno").value,
        finalidade: document.getElementById("finalidade").value,
        quantidade_de_alunos: parseInt(document.getElementById("quantidade_de_alunos").value, 10)
    };

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)
        });

        if (response.ok) {
            document.getElementById("form-reserva").reset();
            await carregarReservas();
        } else {
            const err = await response.json();
            alert(`Erro: ${err.detail || "Não foi possível salvar a reserva."}`);
        }
    } catch (error) {
        console.error("Erro ao conectar ao servidor:", error);
    }
});