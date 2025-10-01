function login() {
  const user = document.getElementById("username").value;
  const pass = document.getElementById("password").value;
  if(user && pass) {
    window.location.href = "dashboard.html";
  } else {
    alert("Digite usuário e senha!");
  }
}

function showContent(section) {
  const content = {
    dashboard: `
      <div class="header">
        <h2>📊 Dashboard</h2>
        <div class="bea-avatar">
          <img src="https://i.pravatar.cc/100?img=5" alt="Bea">
          <span>Bea está online 💬</span>
        </div>
      </div>
      <div class="cards">
        <div class="card-small card-blue"><h3>Clientes</h3><p>152</p></div>
        <div class="card-small card-purple"><h3>Atendimentos</h3><p>27</p></div>
        <div class="card-small card-green"><h3>Faturamento</h3><p>R$ 4.250</p></div>
      </div>
    `,
    clientes: `
      <h2>👩 Clientes</h2>
      <table>
        <tr><th>Nome</th><th>Telefone</th><th>Último Serviço</th><th>Data</th></tr>
        <tr><td>Ana Souza</td><td>(48) 99999-1234</td><td>Coloração</td><td>20/09/2025</td></tr>
        <tr><td>Maria Silva</td><td>(48) 98888-5678</td><td>Corte</td><td>25/09/2025</td></tr>
        <tr><td>João Costa</td><td>(48) 97777-4321</td><td>Barba</td><td>28/09/2025</td></tr>
      </table>
    `,
    agenda: `
      <h2>📅 Agenda</h2>
      <table>
        <tr><th>Cliente</th><th>Serviço</th><th>Data/Hora</th><th>Status</th></tr>
        <tr><td>Ana Souza</td><td>Coloração</td><td>30/09 - 14:00</td><td><span class="tag confirmado">Confirmado</span></td></tr>
        <tr><td>Maria Silva</td><td>Corte</td><td>01/10 - 10:00</td><td><span class="tag pendente">Pendente</span></td></tr>
        <tr><td>João Costa</td><td>Barba</td><td>01/10 - 16:00</td><td><span class="tag cancelado">Cancelado</span></td></tr>
      </table>
    `,
    caixa: `
      <h2>💰 Caixa</h2>
      <table>
        <tr><th>Data</th><th>Descrição</th><th>Tipo</th><th>Valor</th></tr>
        <tr><td>29/09</td><td>Coloração - Ana Souza</td><td>Entrada</td><td>R$ 120,00</td></tr>
        <tr><td>29/09</td><td>Compra de tintas</td><td>Saída</td><td>- R$ 300,00</td></tr>
        <tr><td>28/09</td><td>Corte - Maria Silva</td><td>Entrada</td><td>R$ 80,00</td></tr>
      </table>
    `,
    campanhas: `
      <h2>📢 Campanhas</h2>
      <ul>
        <li>Promoção Outubro Rosa: 20% de desconto em coloração.</li>
        <li>Lembrete automático: clientes sem visita há 30 dias.</li>
        <li>Mensagem de aniversário com cupom de R$ 30.</li>
      </ul>
    `,
    config: `
      <h2>⚙ Configurações</h2>
      <p><strong>Serviços cadastrados:</strong></p>
      <ul>
        <li>Corte - R$ 80</li>
        <li>Coloração - R$ 120</li>
        <li>Manicure - R$ 50</li>
        <li>Barba - R$ 60</li>
      </ul>
    `
  };
  document.getElementById("mainContent").innerHTML = content[section];
}

/* ===================== BOT BEA ===================== */
function toggleChat() {
  const chat = document.getElementById("chatBox");
  chat.style.display = (chat.style.display === "flex") ? "none" : "flex";
}

// Enviar mensagem
function sendMessage() {
  const input = document.getElementById("userMessage");
  const msg = input.value.trim();
  if (!msg) return;

  const messages = document.getElementById("chatMessages");

  // Usuário
  const userMsg = document.createElement("div");
  userMsg.className = "message user";
  userMsg.textContent = msg;
  messages.appendChild(userMsg);
  saveMessage("user", msg);

  // Resposta da Bea
  setTimeout(() => {
    const botMsg = document.createElement("div");
    botMsg.className = "message bot";

    if (msg.toLowerCase().includes("horário")) {
      botMsg.textContent = "Temos horários amanhã às 10h, 14h e 16h ⏰";
    } else if (msg.toLowerCase().includes("preço")) {
      botMsg.textContent = "O corte custa R$80 e a coloração R$120 💇‍♀️";
    } else if (msg.toLowerCase().includes("promo")) {
      botMsg.textContent = "Estamos com 20% de desconto na coloração neste mês 🎉";
    } else {
      botMsg.textContent = "Entendi! Em breve alguém da equipe vai falar com você 😉";
    }

    messages.appendChild(botMsg);
    saveMessage("bot", botMsg.textContent);
    messages.scrollTop = messages.scrollHeight;
  }, 800);

  input.value = "";
}

// Salvar histórico
function saveMessage(sender, text) {
  let history = JSON.parse(localStorage.getItem("beaChat")) || [];
  history.push({ sender, text });
  localStorage.setItem("beaChat", JSON.stringify(history));
}

// Restaurar histórico
window.onload = function() {
  const messages = document.getElementById("chatMessages");
  if (messages) {
    let history = JSON.parse(localStorage.getItem("beaChat")) || [];
    history.forEach(msg => {
      const div = document.createElement("div");
      div.className = "message " + msg.sender;
      div.textContent = msg.text;
      messages.appendChild(div);
    });
  }
}

/* ===================== CAMPANHAS DEMO ===================== */
function enviarCampanha() {
  const clientes = ["Ana Souza", "Maria Silva", "João Costa"];
  const mensagens = document.getElementById("mensagensEnviadas");

  mensagens.innerHTML = ""; // limpa antes

  clientes.forEach((cliente, i) => {
    const li = document.createElement("li");
    li.textContent = `Enviando mensagem para ${cliente}...`;
    mensagens.appendChild(li);

    setTimeout(() => {
      li.textContent = `✅ Mensagem enviada para ${cliente}: "Olá ${cliente}, sentimos sua falta! Volte a nos visitar 💇‍♀️"`;
    }, 1000 * (i + 1));
  });

  // Bea avisa no chat
  const chat = document.getElementById("chatMessages");
  if (chat) {
    const botMsg = document.createElement("div");
    botMsg.className = "message bot";
    botMsg.textContent = "Acabei de disparar 3 lembretes automáticos para clientes inativos 📢";
    chat.appendChild(botMsg);
    chat.scrollTop = chat.scrollHeight;
  }
};
