import os, socket
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"host": socket.gethostname(),
            "entorno": os.getenv("APP_ENV", "sin definir"),
            "usuario": os.getenv("USER", "desconocido")}

@app.route("/guardar")
def guardar():
    with open("/data/nota.txt", "a") as f:
        f.write("registro\n")
    return "guardado"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
