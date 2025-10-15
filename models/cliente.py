from sqlalchemy import Column, Integer, String, Date, DateTime
from datetime import datetime
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=False, unique=True)
    ultimo_servico = Column(String(100))
    data_ultimo = Column(Date)
    origem = Column(String(50), default="importado")
    criado_em = Column(DateTime, default=datetime.now)

