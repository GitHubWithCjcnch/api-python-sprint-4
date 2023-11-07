import os
from db import *
from flask import Flask, jsonify, request
from flask import render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='/home/opc')
CORS(app)


@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    conn = conectar_banco()
    data = request.get_json()
    cpf = data.get('cpf')
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    dt_nasc = data.get('dt_nasc')
    
    inserir_usuario(conn, cpf, nome, email, senha, dt_nasc)
    
    return jsonify({"mensagem": "Usuário criado com sucesso"}), 201

@app.route('/usuarios', methods=['GET'])
def listar_todos_usuarios():
    conn = conectar_banco()
    usuarios = listar_usuarios(conn)
    return jsonify(usuarios)

@app.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def atualizar_um_usuario(id_usuario):
    conn = conectar_banco()
    data = request.get_json()
    cpf = data.get('cpf')
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    dt_nasc = data.get('dt_nasc')
    
    atualizar_usuario(conn, id_usuario, cpf, nome, email, senha, dt_nasc)
    
    return jsonify({"mensagem": f"Usuário com ID {id_usuario} atualizado com sucesso"})

@app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def excluir_um_usuario(id_usuario):
    conn = conectar_banco()
    excluir_usuario(conn, id_usuario)
    return jsonify({"mensagem": f"Usuário com ID {id_usuario} excluído com sucesso"})

@app.route('/guinchos', methods=['POST'])
def criar_guincho():
    data = request.get_json()
    peso = data.get('peso')
    tipo = data.get('tipo')
    disponibilidade = data.get('disponibilidade')
    
    inserir_guincho(conn, peso, tipo, disponibilidade)
    
    return jsonify({"mensagem": "Guincho criado com sucesso"}), 201

@app.route('/guinchos', methods=['GET'])
def listar_todos_guinchos():
    guinchos = listar_guinchos(conn)
    return jsonify(guinchos)

@app.route('/guinchos/<int:id_guincho>', methods=['PUT'])
def atualizar_um_guincho(id_guincho):
    data = request.get_json()
    peso = data.get('peso')
    tipo = data.get('tipo')
    disponibilidade = data.get('disponibilidade')
    
    atualizar_guincho(conn, id_guincho, peso, tipo, disponibilidade)
    
    return jsonify({"mensagem": f"Guincho com ID {id_guincho} atualizado com sucesso"})

@app.route('/guinchos/<int:id_guincho>', methods=['DELETE'])
def excluir_um_guincho(id_guincho):
    excluir_guincho(conn, id_guincho)
    return jsonify({"mensagem": f"Guincho com ID {id_guincho} excluído com sucesso"})

@app.route('/enderecos', methods=['POST'])
def criar_endereco():
    data = request.get_json()
    cep = data.get('cep')
    rua = data.get('rua')
    num = data.get('num')
    logradouro = data.get('logradouro')
    bairro = data.get('bairro')
    cidade = data.get('cidade')
    municipio = data.get('municipio')
    uf = data.get('uf')
    pais = data.get('pais')
    
    inserir_endereco(conn, cep, rua, num, logradouro, bairro, cidade, municipio, uf, pais)
    
    return jsonify({"mensagem": "Endereço criado com sucesso"}), 201

@app.route('/enderecos', methods=['GET'])
def listar_todos_enderecos():
    enderecos = listar_enderecos(conn)
    return jsonify(enderecos)

@app.route('/enderecos/<int:id_endereco>', methods=['PUT'])
def atualizar_um_endereco(id_endereco):
    data = request.get_json()
    cep = data.get('cep')
    rua = data.get('rua')
    num = data.get('num')
    logradouro = data.get('logradouro')
    bairro = data.get('bairro')
    cidade = data.get('cidade')
    municipio = data.get('municipio')
    uf = data.get('uf')
    pais = data.get('pais')
    
    atualizar_endereco(conn, id_endereco, cep, rua, num, logradouro, bairro, cidade, municipio, uf, pais)
    
    return jsonify({"mensagem": f"Endereço com ID {id_endereco} atualizado com sucesso"})

@app.route('/enderecos/<int:id_endereco>', methods=['DELETE'])
def excluir_um_endereco(id_endereco):
    excluir_endereco(conn, id_endereco)
    return jsonify({"mensagem": f"Endereço com ID {id_endereco} excluído com sucesso"})

@app.route('/prestadores', methods=['POST'])
def criar_prestador_servico():
    data = request.get_json()
    cpf = data.get('cpf')
    nome = data.get('nome')
    servico_oferecido = data.get('servico_oferecido')
    
    inserir_prestador_servico(conn, cpf, nome, servico_oferecido)
    
    return jsonify({"mensagem": "Prestador de serviço criado com sucesso"}), 201

@app.route('/prestadores', methods=['GET'])
def listar_todos_prestadores_servico():
    prestadores = listar_prestadores_servico(conn)
    return jsonify(prestadores)

@app.route('/prestadores/<int:id_prestador_servico>', methods=['PUT'])
def atualizar_um_prestador_servico(id_prestador_servico):
    data = request.get_json()
    cpf = data.get('cpf')
    nome = data.get('nome')
    servico_oferecido = data.get('servico_oferecido')
    
    atualizar_prestador_servico(conn, id_prestador_servico, cpf, nome, servico_oferecido)
    
    return jsonify({"mensagem": f"Prestador de serviço com ID {id_prestador_servico} atualizado com sucesso"})

@app.route('/prestadores/<int:id_prestador_servico>', methods=['DELETE'])
def excluir_um_prestador_servico(id_prestador_servico):
    excluir_prestador_servico(conn, id_prestador_servico)
    return jsonify({"mensagem": f"Prestador de serviço com ID {id_prestador_servico} excluído com sucesso"})

@app.route('/tipos-veiculo', methods=['POST'])
def criar_tipo_veiculo():
    data = request.get_json()
    nome_tipo_veiculo = data.get('nome_tipo_veiculo')
    
    inserir_tipo_veiculo(conn, nome_tipo_veiculo)
    
    return jsonify({"mensagem": "Tipo de veículo criado com sucesso"}), 201

@app.route('/tipos-veiculo', methods=['GET'])
def listar_todos_tipos_veiculo():
    tipos = listar_tipos_veiculo(conn)
    return jsonify(tipos)

@app.route('/tipos-veiculo/<int:id_tipo_veiculo>', methods=['PUT'])
def atualizar_um_tipo_veiculo(id_tipo_veiculo):
    data = request.get_json()
    nome_tipo_veiculo = data.get('nome_tipo_veiculo')
    
    atualizar_tipo_veiculo(conn, id_tipo_veiculo, nome_tipo_veiculo)
    
    return jsonify({"mensagem": f"Tipo de veículo com ID {id_tipo_veiculo} atualizado com sucesso"})

@app.route('/tipos-veiculo/<int:id_tipo_veiculo>', methods=['DELETE'])
def excluir_um_tipo_veiculo(id_tipo_veiculo):
    excluir_tipo_veiculo(conn, id_tipo_veiculo)
    return jsonify({"mensagem": f"Tipo de veículo com ID {id_tipo_veiculo} excluído com sucesso"})

@app.route('/veiculos', methods=['POST'])
def criar_veiculo():
    data = request.get_json()
    placa_veiculo = data.get('placa_veiculo')
    peso_veiculo = data.get('peso_veiculo')
    comprimento_veiculo = data.get('comprimento_veiculo')
    altura_veiculo = data.get('altura_veiculo')
    modelo_veiculo = data.get('modelo_veiculo')
    chassiAlongado_veiculo = data.get('chassiAlongado_veiculo')
    qtdEixos_veiculo = data.get('qtdEixos_veiculo')
    capacidadeCarga_veiculo = data.get('capacidadeCarga_veiculo')
    disponibilidade_veiculo = data.get('disponibilidade_veiculo')
    id_tipoVeiculo_veiculo = data.get('id_tipoVeiculo_veiculo')
    
    inserir_veiculo(conn, placa_veiculo, peso_veiculo, comprimento_veiculo, altura_veiculo, modelo_veiculo, chassiAlongado_veiculo, qtdEixos_veiculo, capacidadeCarga_veiculo, disponibilidade_veiculo, id_tipoVeiculo_veiculo)
    
    return jsonify({"mensagem": "Veículo criado com sucesso"}), 201

@app.route('/veiculos', methods=['GET'])
def listar_todos_veiculos():
    veiculos = listar_veiculos(conn)
    return jsonify(veiculos)

@app.route('/veiculos/<int:id_veiculo>', methods=['PUT'])
def atualizar_um_veiculo(id_veiculo):
    data = request.get_json()
    placa_veiculo = data.get('placa_veiculo')
    peso_veiculo = data.get('peso_veiculo')
    comprimento_veiculo = data.get('comprimento_veiculo')
    altura_veiculo = data.get('altura_veiculo')
    modelo_veiculo = data.get('modelo_veiculo')
    chassiAlongado_veiculo = data.get('chassiAlongado_veiculo')
    qtdEixos_veiculo = data.get('qtdEixos_veiculo')
    capacidadeCarga_veiculo = data.get('capacidadeCarga_veiculo')
    disponibilidade_veiculo = data.get('disponibilidade_veiculo')
    id_tipoVeiculo_veiculo = data.get('id_tipoVeiculo_veiculo')
    
    atualizar_veiculo(conn, id_veiculo, placa_veiculo, peso_veiculo, comprimento_veiculo, altura_veiculo, modelo_veiculo, chassiAlongado_veiculo, qtdEixos_veiculo, capacidadeCarga_veiculo, disponibilidade_veiculo, id_tipoVeiculo_veiculo)
    
    return jsonify({"mensagem": f"Veículo com ID {id_veiculo} atualizado com sucesso"})

@app.route('/veiculos/<int:id_veiculo>', methods=['DELETE'])
def excluir_um_veiculo(id_veiculo):
    excluir_veiculo(conn, id_veiculo)
    return jsonify({"mensagem": f"Veículo com ID {id_veiculo} excluído com sucesso"})

@app.route('/localizacoes', methods=['POST'])
def criar_localizacao():
    data = request.get_json()
    tipo_terreno_localizacao = data.get('tipo_terreno_localizacao')
    desc_localizacao = data.get('desc_localizacao')
    id_endereco = data.get('id_endereco')
    
    inserir_localizacao(conn, tipo_terreno_localizacao, desc_localizacao, id_endereco)
    
    return jsonify({"mensagem": "Localização criada com sucesso"}), 201

@app.route('/localizacoes', methods=['GET'])
def listar_todas_localizacoes():
    localizacoes = listar_localizacoes(conn)
    return jsonify(localizacoes)

@app.route('/localizacoes/<int:id_localizacao>', methods=['PUT'])
def atualizar_uma_localizacao(id_localizacao):
    data = request.get_json()
    tipo_terreno_localizacao = data.get('tipo_terreno_localizacao')
    desc_localizacao = data.get('desc_localizacao')
    id_endereco = data.get('id_endereco')
    
    atualizar_localizacao(conn, id_localizacao, tipo_terreno_localizacao, desc_localizacao, id_endereco)
    
    return jsonify({"mensagem": f"Localização com ID {id_localizacao} atualizada com sucesso"})

@app.route('/localizacoes/<int:id_localizacao>', methods=['DELETE'])
def excluir_uma_localizacao(id_localizacao):
    excluir_localizacao(conn, id_localizacao)
    return jsonify({"mensagem": f"Localização com ID {id_localizacao} excluída com sucesso"})

@app.route('/seguros', methods=['POST'])
def criar_seguro():
    data = request.get_json()
    data_inicio_seguro = data.get('data_inicio_seguro')
    data_termino_seguro = data.get('data_termino_seguro')
    valor_cobertura_seguro = data.get('valor_cobertura_seguro')
    id_usuario = data.get('id_usuario')
    id_veiculo = data.get('id_veiculo')
    
    inserir_seguro(conn, data_inicio_seguro, data_termino_seguro, valor_cobertura_seguro, id_usuario, id_veiculo)
    
    return jsonify({"mensagem": "Seguro criado com sucesso"}), 201

@app.route('/seguros', methods=['GET'])
def listar_todos_seguros():
    seguros = listar_seguros(conn)
    return jsonify(seguros)

@app.route('/seguros/<int:id_Seguro>', methods=['PUT'])
def atualizar_um_seguro(id_Seguro):
    data = request.get_json()
    data_inicio_seguro = data.get('data_inicio_seguro')
    data_termino_seguro = data.get('data_termino_seguro')
    valor_cobertura_seguro = data.get('valor_cobertura_seguro')
    id_usuario = data.get('id_usuario')
    id_veiculo = data.get('id_veiculo')
    
    atualizar_seguro(conn, id_Seguro, data_inicio_seguro, data_termino_seguro, valor_cobertura_seguro, id_usuario, id_veiculo)
    
    return jsonify({"mensagem": f"Seguro com ID {id_Seguro} atualizado com sucesso"})

@app.route('/seguros/<int:id_Seguro>', methods=['DELETE'])
def excluir_um_seguro(id_Seguro):
    excluir_seguro(conn, id_Seguro)
    return jsonify({"mensagem": f"Seguro com ID {id_Seguro} excluído com sucesso"})

@app.route('/solicitacoes-guincho', methods=['POST'])
def criar_solicitacao_guincho():
    data = request.get_json()
    descricao_solicitacao_guincho = data.get('descricao_solicitacao_guincho')
    id_localizacao = data.get('id_localizacao')
    id_usuario = data.get('id_usuario')
    id_veiculo = data.get('id_veiculo')
    
    inserir_solicitacao_guincho(conn, descricao_solicitacao_guincho, id_localizacao, id_usuario, id_veiculo)
    
    return jsonify({"mensagem": "Solicitação de guincho criada com sucesso"}), 201

@app.route('/solicitacoes-guincho', methods=['GET'])
def listar_todas_solicitacoes_guincho():
    solicitacoes = listar_solicitacoes_guincho(conn)
    return jsonify(solicitacoes)

@app.route('/solicitacoes-guincho/<int:id_solicitacao_guincho>', methods=['PUT'])
def atualizar_uma_solicitacao_guincho(id_solicitacao_guincho):
    data = request.get_json()
    descricao_solicitacao_guincho = data.get('descricao_solicitacao_guincho')
    id_localizacao = data.get('id_localizacao')
    id_usuario = data.get('id_usuario')
    id_veiculo = data.get('id_veiculo')
    
    atualizar_solicitacao_guincho(conn, id_solicitacao_guincho, descricao_solicitacao_guincho, id_localizacao, id_usuario, id_veiculo)
    
    return jsonify({"mensagem": f"Solicitação de guincho com ID {id_solicitacao_guincho} atualizada com sucesso"})

@app.route('/solicitacoes-guincho/<int:id_solicitacao_guincho>', methods=['DELETE'])
def excluir_uma_solicitacao_guincho(id_solicitacao_guincho):
    excluir_solicitacao_guincho(conn, id_solicitacao_guincho)
    return jsonify({"mensagem": f"Solicitação de guincho com ID {id_solicitacao_guincho} excluída com sucesso"})

@app.route('/situacoes-solicitacao-guincho', methods=['POST'])
def criar_situacao_solicitacao_guincho():
    data = request.get_json()
    id_solicitacao_guincho = data.get('id_solicitacao_guincho')
    id_guincho = data.get('id_guincho')
    id_prestador_servico = data.get('id_prestador_servico')
    
    inserir_situacao_solicitacao_guincho(conn, id_solicitacao_guincho, id_guincho, id_prestador_servico)
    
    return jsonify({"mensagem": "Situação de solicitação de guincho criada com sucesso"}), 201

@app.route('/situacoes-solicitacao-guincho', methods=['GET'])
def listar_todas_situacoes_solicitacao_guincho():
    situacoes = listar_situacoes_solicitacao_guincho(conn)
    return jsonify(situacoes)

@app.route('/situacoes-solicitacao-guincho/<int:id_situacao_solicitacao>', methods=['PUT'])
def atualizar_uma_situacao_solicitacao_guincho(id_situacao_solicitacao):
    data = request.get_json()
    id_solicitacao_guincho = data.get('id_solicitacao_guincho')
    id_guincho = data.get('id_guincho')
    id_prestador_servico = data.get('id_prestador_servico')
    
    atualizar_situacao_solicitacao_guincho(conn, id_situacao_solicitacao, id_solicitacao_guincho, id_guincho, id_prestador_servico)
    
    return jsonify({"mensagem": f"Situação de solicitação de guincho com ID {id_situacao_solicitacao} atualizada com sucesso"})

@app.route('/situacoes-solicitacao-guincho/<int:id_situacao_solicitacao>', methods=['DELETE'])
def excluir_uma_situacao_solicitacao_guincho(id_situacao_solicitacao):
    excluir_situacao_solicitacao_guincho(conn, id_situacao_solicitacao)
    return jsonify({"mensagem": f"Situação de solicitação de guincho com ID {id_situacao_solicitacao} excluída com sucesso"})


if __name__ == '__main__':
    app.run()
