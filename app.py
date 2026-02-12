import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Carrega variáveis do .env (para ambiente local ou Render)
load_dotenv()

from database import init_db
from routes.clientes import bp_clientes
from routes.campanhas import bp_campanhas
from routes.bot import bp_bot

# ==========================================================
# 💡 Inicialização do aplicativo Flask
# ==========================================================
app = Flask(__name__)  # ✅ Corrigido: __name__, não "name"
CORS(app)

# Cria as tabelas automaticamente no banco (se não existirem)
init_db()

# ==========================================================
# 🔗 Registro das rotas
# ==========================================================
app.register_blueprint(bp_clientes, url_prefix='/api')
app.register_blueprint(bp_campanhas, url_prefix='/api')
app.register_blueprint(bp_bot, url_prefix='/api')

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
    # Só use debug=True em desenvolvimento!
    app.run(host="0.0.0.0", port=port, debug=(os.getenv("FLASK_ENV") != "production"))
