from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import requests

app = Flask(__name__)
CORS(app)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ana@1234",  
    database="vendas_db"
)
cursor = db.cursor()

@app.route("/")
def home():
    return "API de Vendas conectada ao MySQL com sucesso!"

# ROTA GET - Listar clientes
@app.route("/clientes", methods=["GET"])
def listar_clientes():
    cursor.execute("SELECT id, nome, cidade, total_compras FROM clientes")
    resultados = cursor.fetchall()
    clientes = [
        {
            "id": r[0],
            "nome": r[1],
            "cidade": r[2],
            "total_compras": float(r[3]) if r[3] is not None else 0.0
        }
        for r in resultados
    ]
    return jsonify(clientes)

# ROTA POST - Adicionar cliente
@app.route("/clientes", methods=["POST"])
def adicionar_cliente():
    data = request.get_json()
    nome = data.get("nome")
    cidade = data.get("cidade")
    total_compras = data.get("total_compras")

    cursor.execute(
        "INSERT INTO clientes (nome, cidade, total_compras) VALUES (%s, %s, %s)",
        (nome, cidade, total_compras)
    )
    db.commit()
    return jsonify({"mensagem": "Cliente adicionado com sucesso"}), 201

# ROTA PUT - Editar cliente
@app.route("/clientes/<int:id>", methods=["PUT"])
def editar_cliente(id):
    data = request.get_json()
    nome = data.get("nome")
    cidade = data.get("cidade")
    total_compras = data.get("total_compras")

    cursor.execute(
        "UPDATE clientes SET nome=%s, cidade=%s, total_compras=%s WHERE id=%s",
        (nome, cidade, total_compras, id)
    )
    db.commit()
    return jsonify({"mensagem": "Cliente atualizado com sucesso"})

# ROTA DELETE - Excluir cliente
@app.route("/clientes/<int:id>", methods=["DELETE"])
def deletar_cliente(id):
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
    db.commit()
    return jsonify({"mensagem": "Cliente excluído com sucesso"})

# ROTA GET - Cotação do dólar (via API externa)
@app.route("/cotacao-dolar", methods=["GET"])
def pegar_cotacao():
    try:
        resposta = requests.get("http://localhost:5001/cotacao")
        dados = resposta.json()
        return jsonify({"cotacao": dados["cotacao_dolar"]})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
