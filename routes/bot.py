from flask import Blueprint, request, jsonify

bp_bot = Blueprint("bot", __name__, url_prefix="/api/bot")

@bp_bot.route("/mensagem", methods=["POST"])
def responder():
    msg = request.json.get("mensagem", "").lower()
    if "horário" in msg:
        resposta = "Temos horários amanhã às 10h, 14h e 16h ⏰"
    elif "preço" in msg:
        resposta = "O corte custa R$80 e a coloração R$120 💇‍♀️"
    else:
        resposta = "Oi! 😊 Eu sou a Bea. Posso te ajudar com horários, preços e promoções."
    return jsonify({"resposta": resposta})

