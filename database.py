import os
import pymysql.cursors

# ==========================================
# 💾 Configuração do Banco de Dados (MySQL)
# NousBe API - Nous Tecnologia
# ==========================================

def get_db_connection():
    """
    Retorna uma nova conexão com o banco de dados MySQL.
    Usa variáveis de ambiente para configuração.
    """
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASS", ""),
        database=os.getenv("DB_NAME", "nousbe_db"),
        port=int(os.getenv("DB_PORT", 3306)),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
        connect_timeout=10,
        read_timeout=10,
        write_timeout=10
    )

def init_db():
    """
    Cria as tabelas necessárias se ainda não existirem.
    Executa CREATE TABLE IF NOT EXISTS diretamente via SQL.
    """
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            # Tabela de clientes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    telefone VARCHAR(20) NOT NULL UNIQUE,
                    ultimo_servico VARCHAR(100),
                    data_ultimo DATE,
                    origem VARCHAR(50) DEFAULT 'importado',
                    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
                ) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
            """)

            # Tabela de campanhas
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS campanhas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100),
                    mensagem TEXT,
                    total_enviados INT DEFAULT 0,
                    total_falhas INT DEFAULT 0,
                    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
                ) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
            """)

            # Tabela de mensagens individuais (opcional, mas recomendado)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS mensagens (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    cliente_id INT NOT NULL,
                    campanha_id INT,
                    mensagem_enviada TEXT,
                    status ENUM('enviado', 'falha', 'entregue', 'lido') DEFAULT 'enviado',
                    erro TEXT,
                    data_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE,
                    FOREIGN KEY (campanha_id) REFERENCES campanhas(id) ON DELETE SET NULL
                ) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
            """)

        print("✅ Tabelas verificadas/criadas com sucesso.")
    finally:
        conn.close()

# ==========================================
# 🧩 Teste rápido de conexão
# ==========================================
if __name__ == "__main__":
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            if result:
                print(f"✅ Conexão com o banco '{os.getenv('DB_NAME', 'nousbe_db')}' bem-sucedida!")
    except Exception as e:
        print(f"❌ Erro ao conectar ao banco: {e}")
    finally:
        conn.close()
