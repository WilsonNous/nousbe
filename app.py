from flask import Flask
from flask_cors import CORS
from database import Base, engine
from routes.clientes import bp_clientes
from routes.campanhas import bp_campanhas
from routes.bot import bp_bot

app = Flask(__name__)
CORS(app)

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Registrar rotas
app.register_blueprint(bp_clientes)
app.register_blueprint(bp_campanhas)
app.register_blueprint(bp_bot)

@app.route("/")
def index():
    return {"status": "NousBe API ativa 🚀"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

