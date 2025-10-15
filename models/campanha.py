from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from database import Base

class Campanha(Base):
    __tablename__ = "campanhas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    mensagem = Column(Text)
    total_enviados = Column(Integer, default=0)
    total_falhas = Column(Integer, default=0)
    data_criacao = Column(DateTime, default=datetime.now)

