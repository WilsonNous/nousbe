from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ajustar conforme suas credenciais HostGator
DB_USER = "root"
DB_PASS = "senha"
DB_HOST = "localhost"
DB_NAME = "nousbe_db"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

