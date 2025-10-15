import pandas as pd
from models.cliente import Cliente

def importar_clientes(session, caminho_arquivo):
    df = pd.read_excel(caminho_arquivo)
    inseridos = 0

    for _, row in df.iterrows():
        nome = str(row.get("Nome", "")).strip()
        telefone = str(row.get("Telefone", "")).strip().replace(" ", "").replace("-", "")
        if not telefone:
            continue
        if not session.query(Cliente).filter_by(telefone=telefone).first():
            session.add(Cliente(nome=nome, telefone=telefone))
            inseridos += 1
    session.commit()
    return inseridos
