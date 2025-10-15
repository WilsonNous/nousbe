from flask import Blueprint, request, jsonify
from database import SessionLocal
from models.cliente import Cliente
from models.campanha import Campanha
from services.whatsapp_service import enviar_mensagem

bp_campanhas = Blueprint("campanhas", __name__, url_prefix="/api/campanhas")

@bp_campanhas.route("/", methods=["POST"])
def criar_campanha():
    session = SessionLocal()
    data = request.json
    campanha = Campanha(nome=data.get("nome"), mensagem=data.get("mensagem"))
    session.add(campanha)
    session.commit()
    return jsonify({"id": campanha.id, "mensagem": "Campanha criada"}), 201

@bp_campanhas.route("/<int:id>/executar", methods=["POST"])
def executar(id):
    session = SessionLocal()
    campanha = session.query(Campanha).get(id)
    if not campanha:
        return jsonify({"erro": "Campanha não encontrada"}), 404

    clientes = session.query(Cliente).all()
    enviados, falhas = 0, 0
    logs = []

    for c in clientes:
        result = enviar_mensagem(c.telefone, campanha.mensagem)
        if result["status"] == "SENT":
            enviados += 1
        else:
            falhas += 1
        logs.append({"cliente": c.nome, "status": result["status"]})

    campanha.total_enviados = enviados
    campanha.total_falhas = falhas
    session.commit()
    session.close()

    return jsonify({
        "mensagem": "Campanha executada",
        "enviados": enviados,
        "falhas": falhas,
        "logs": logs
    })
