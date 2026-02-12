import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Carrega variáveis do .env (apenas se estiver em ambiente local)
if os.getenv("RENDER") is None:
    load_dotenv()

from database import init_db
from routes.clientes import bp_clientes
from routes.campanhas import bp_campanhas
from routes.bot import bp_bot

# ==========================================================
# 💡 Inicialização do aplicativo Flask
# ==========================================================
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # Mantém a ordem dos campos no JSON

# Configura CORS com segurança (ajuste as origens em produção)
CORS(app, origins=[
    "http://localhost:3000",      # Frontend local
    "https://seu-dashboard.com"   # Substitua pelo domínio real do dashboard
] if os.getenv("FLASK_ENV") == "production" else "*")

# Cria as tabelas no banco (executa apenas uma vez na inicialização)
try:
    init_db()
except Exception as e:
    print(f"⚠️ Aviso: falha ao inicializar o banco de dados: {e}")

# ==========================================================
# 🔗 Registro das rotas
# ==========================================================
app.register_blueprint(bp_clientes, url_prefix='/api')
app.register_blueprint(bp_campanhas, url_prefix='/api')
app.register_blueprint(bp_bot, url_prefix='/api')

# ==========================================================
# 🏁 Rota de verificação (health check)
# ==========================================================
@app.route("/")
def index():
    return {
        "status": "NousBe API ativa 🚀",
        "ambiente": os.getenv("FLASK_ENV", "development"),
        "banco": os.getenv("DB_NAME", "nousbe_db"),
        "versao": "1.0.0"
    }

# ==========================================================
# 🔥 Execução da aplicação
# ==========================================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.getenv("FLASK_ENV") != "production"
    print(f"🚀 Iniciando NousBe API na porta {port} | Ambiente: {'produção' if not debug_mode else 'desenvolvimento'}")
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
