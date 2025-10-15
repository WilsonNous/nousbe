import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ==========================================
# 💾 Configuração do Banco de Dados (MySQL)
# NousBe API - Nous Tecnologia
# ==========================================

# Lê variáveis de ambiente
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "nousbe_db")

# Monta URL de conexão compatível com o SQLAlchemy + PyMySQL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"

# Cria engine e sessão
engine = create_engine(
    DATABASE_URL,
    echo=False,          # pode mudar para True para debug SQL
    pool_pre_ping=True,  # mantém conexões ativas
    pool_recycle=3600    # reinicia a cada hora para evitar timeout
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ==========================================
# 🧠 Função utilitária para criar o schema
# ==========================================
def init_db():
    """Cria todas as tabelas definidas nos models."""
    from models import cliente, campanha  # importa os modelos
    Base.metadata.create_all(bind=engine)
    print("✅ Tabelas criadas ou já existentes no banco de dados.")

# ==========================================
# 🧩 Teste rápido de conexão
# ==========================================
if __name__ == "__main__":
    try:
        connection = engine.connect()
        print(f"✅ Conectado com sucesso ao banco: {DB_NAME} ({DB_HOST})")
        connection.close()
    except Exception as e:
        print(f"❌ Erro ao conectar ao banco: {e}")
