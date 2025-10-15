import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Carrega variáveis do .env (para ambiente local ou Render)
load_dotenv()

from database import Base, engine, init_db
from routes.clientes import bp_clientes
from routes.campanhas import bp_campanhas
from routes.bot import bp_bot

# ==========================================================
# 💡 Inicialização do aplicativo Flask
# ==========================================================
app = Flask(__name__)
CORS(app)

# Cria as tabelas automaticamente no banco (se não existirem)
init_db()

# ==========================================================
# 🔗 Registro das rotas
# ==========================================================
app.register_blueprint(bp_clientes)
app.register_blueprint(bp_campanhas)
app.register_blueprint(bp_bot)

# ==========================================================
# 🏁 Rota de verificação
# ==========================================================
@app.route("/")
def index():
    return {
        "status": "NousBe API ativa 🚀",
        "ambiente": os.getenv("FLASK_ENV", "development"),
        "banco": os.getenv("DB_NAME", "nousbe_db"),
        "host": os.getenv("DB_HOST", "localhost")
    }

# ==========================================================
# 🔥 Execução da aplicação
# ==========================================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Iniciando NousBe API na porta {port}")
    app.run(host="0.0.0.0", port=port)
