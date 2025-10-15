from flask import Blueprint, request, jsonify
from database import SessionLocal
from models.cliente import Cliente
from services.importer import importar_clientes

bp_clientes = Blueprint("clientes", __name__, url_prefix="/api/clientes")

@bp_clientes.route("/", methods=["GET"])
def listar_clientes():
    session = SessionLocal()
    clientes = session.query(Cliente).all()
    data = [{"id": c.id, "nome": c.nome, "telefone": c.telefone} for c in clientes]
    session.close()
    return jsonify(data)

@bp_clientes.route("/importar", methods=["POST"])
def importar():
    session = SessionLocal()
    if "arquivo" not in request.files:
        return jsonify({"erro": "Nenhum arquivo enviado"}), 400
    arquivo = request.files["arquivo"]
    caminho = f"/tmp/{arquivo.filename}"
    arquivo.save(caminho)
    qtd = importar_clientes(session, caminho)
    session.close()
    return jsonify({"mensagem": f"{qtd} clientes importados com sucesso"})

