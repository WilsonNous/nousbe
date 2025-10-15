# 📘 NousBe API
**Um projeto da Nous Tecnologia — Tecnologia com Propósito**

---

### ✨ Sobre o projeto

O **NousBe API** é o backend oficial do sistema **NousBe**, uma solução desenvolvida pela **Nous Tecnologia** para gestão de salões de beleza, barbearias e centros de estética.

Mais do que um sistema de gestão, o NousBe reflete a filosofia da Nous:  
> “Tecnologia com propósito, negócios com essência.”  

Seu objetivo é simplificar o atendimento, automatizar a comunicação e criar uma experiência acolhedora entre clientes e profissionais, inspirada pela fé, excelência e serviço.

---

### 🚀 Funcionalidades principais (MVP)

| Módulo | Descrição |
|--------|------------|
| 🧾 **Importação de Clientes** | Importa base de clientes diretamente de planilhas Excel/CSV (ex: exportadas do GENDO). |
| 💬 **Disparo de Mensagens (Campanhas)** | Envio em massa de mensagens via **WhatsApp API (Z-API)** para campanhas de lembrete, promoção ou fidelização. |
| 🤖 **IA Bea (Assistente Virtual)** | IA leve integrada ao backend, capaz de responder dúvidas simples e automatizar o primeiro atendimento. |
| 📊 **Dashboard de Controle** | Interface frontend (em outro módulo) conectada à API, exibindo métricas, agendamentos e mensagens enviadas. |

---

### 🏗️ Estrutura do projeto

```
nousbe_api/
│
├── app.py
├── database.py
├── requirements.txt
│
├── routes/
│   ├── clientes.py
│   ├── campanhas.py
│   ├── bot.py
│   └── __init__.py
│
├── services/
│   ├── whatsapp_service.py
│   ├── importer.py
│   └── __init__.py
│
└── models/
    ├── cliente.py
    ├── campanha.py
    └── __init__.py
```

---

### 📂 Estrutura do Banco (`nousbe_db`)

```sql
CREATE DATABASE IF NOT EXISTS nousbe_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE nousbe_db;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL UNIQUE,
    ultimo_servico VARCHAR(100),
    data_ultimo DATE,
    origem VARCHAR(50) DEFAULT 'importado',
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE campanhas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    mensagem TEXT,
    total_enviados INT DEFAULT 0,
    total_falhas INT DEFAULT 0,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

### 💙 Filosofia Nous Tecnologia

> “A Nous nasceu com um propósito simples e profundo:  
> servir pessoas e negócios com tecnologia inspirada pelo Reino de Deus.”  

Cada projeto desenvolvido é guiado por **propósito, serviço, excelência e fé**.  
O NousBe é a expressão dessa visão aplicada à área da beleza —  
tecnologia para servir, não apenas operar.
