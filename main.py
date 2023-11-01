import os
from flask import Flask, jsonify, request
from flask import render_template
from flask_cors import CORS
import cx_Oracle

app = Flask(__name__, template_folder='/home/opc')
CORS(app)

db_connection = cx_Oracle.connect('RM552392', '120304', 'oracle.fiap.com.br:1521/ORCL')

def execute_query(query, *args):
    cursor = db_connection.cursor()
    cursor.execute(query, args)
    db_connection.commit()
    cursor.close()

@app.route('/apiPython/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    try:
        query = "INSERT INTO USUARIO (cpf_usuario, nome_usuario, email_usuario, senha_usuario, dt_nasc_usuario) VALUES (:1, :2, :3, :4, :5)"
        execute_query(query, data['cpf_usuario'], data['nome_usuario'], data['email_usuario'], data['senha_usuario'], data['dt_nasc_usuario'])
        return jsonify({"message": "Usuário criado com sucesso"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/apiPython/usuarios/<int:id_usuario>', methods=['GET'])
def obter_usuario(id_usuario):
    try:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM USUARIO WHERE id_usuario = :1", (id_usuario,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            columns = [desc[0] for desc in cursor.description]
            user = dict(zip(columns, result))
            return jsonify(user)
        else:
            return jsonify({"message": "Usuário não encontrado"}, 404)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/apiPython/usuarios/<int:id_usuario>', methods=['PUT'])
def atualizar_usuario(id_usuario):
    data = request.json
    try:
        query = "UPDATE USUARIO SET cpf_usuario = :1, nome_usuario = :2, email_usuario = :3, senha_usuario = :4, dt_nasc_usuario = :5 WHERE id_usuario = :6"
        execute_query(query, data['cpf_usuario'], data['nome_usuario'], data['email_usuario'], data['senha_usuario'], data['dt_nasc_usuario'], id_usuario)
        return jsonify({"message": "Usuário atualizado com sucesso"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/apiPython/usuarios/<int:id_usuario>', methods=['DELETE'])
def excluir_usuario(id_usuario):
    try:
        query = "DELETE FROM USUARIO WHERE id_usuario = :1"
        execute_query(query, id_usuario)
        return jsonify({"message": "Usuário excluído com sucesso"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)