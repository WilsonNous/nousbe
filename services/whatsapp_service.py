import requests

ZAPI_INSTANCE = "YOUR_INSTANCE_ID"
ZAPI_TOKEN = "YOUR_TOKEN"
ZAPI_URL = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-text"

def enviar_mensagem(numero, texto):
    payload = {
        "phone": numero,
        "message": texto
    }
    try:
        r = requests.post(ZAPI_URL, json=payload, timeout=10)
        if r.status_code == 200:
            return {"status": "SENT", "response": r.json()}
        else:
            return {"status": "ERROR", "response": r.text}
    except Exception as e:
        return {"status": "ERROR", "response": str(e)}

