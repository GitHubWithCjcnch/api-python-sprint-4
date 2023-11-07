import sqlite3

def conectar_banco():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS USUARIO (
          id_usuario INTEGER PRIMARY KEY,
          cpf_usuario NUMERIC NOT NULL,
          nome_usuario TEXT NOT NULL,
          email_usuario TEXT NOT NULL,
          senha_usuario TEXT NOT NULL,
          dt_nasc_usuario DATETIME NOT NULL
        );"""
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS GUINCHO (
          id_guincho INTEGER PRIMARY KEY,
          peso_guincho NUMERIC(10, 2),
          tipo_guincho TEXT,
          disponibilidade_guincho NUMERIC(1, 0)
        );
      """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ENDERECO (
          id_endereco INTEGER PRIMARY KEY,
          cep_endereco TEXT NOT NULL,
          rua_endereco TEXT NOT NULL,
          num_endereco TEXT,
          logradouro_endereco TEXT,
          bairro_endereco TEXT NOT NULL,
          cidade_endereco TEXT NOT NULL,
          municipio_endereco TEXT NOT NULL,
          uf_endereco TEXT(2) NOT NULL,
          pais_endereco TEXT NOT NULL
        );
      """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS PRESTADOR_SERVICO (
          id_prestador_servico INTEGER PRIMARY KEY,
          cpf_prestador_servico NUMERIC(11, 0),
          nome_prestador_servico TEXT NOT NULL,
          servico_oferecido_prestador TEXT(30)
        );
      """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS TIPO_VEICULO (
          id_tipo_veiculo INTEGER PRIMARY KEY,
          nome_tipo_veiculo TEXT NOT NULL
        );
      """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS VEICULO (
          id_veiculo INTEGER PRIMARY KEY,
          placa_veiculo TEXT NOT NULL,
          peso_veiculo NUMERIC(10, 2),
          comprimento_veiculo NUMERIC(10, 2),
          altura_veiculo NUMERIC(10, 2),
          modelo_veiculo TEXT(50),
          chassiAlongado_veiculo NUMERIC(1, 0),
          qtdEixos_veiculo NUMERIC(1, 0),
          capacidadeCarga_veiculo NUMERIC(10, 0),
          disponibilidade_veiculo NUMERIC(1, 0),
          id_tipoVeiculo_veiculo INTEGER,
          FOREIGN KEY (id_tipoVeiculo_veiculo) REFERENCES TIPO_VEICULO(id_tipo_veiculo)
        );
      """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS LOCALIZACAO (
          id_localizacao INTEGER PRIMARY KEY,
          tipo_terreno_localizacao TEXT(50),
          desc_localizacao TEXT NOT NULL,
          id_endereco INTEGER,
          FOREIGN KEY (id_endereco) REFERENCES ENDERECO(id_endereco)
        );
      """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS SEGURO (
          id_Seguro INTEGER PRIMARY KEY,
          data_inicio_seguro DATE,
          data_termino_seguro DATE,
          valor_cobertura_seguro NUMERIC(10, 2),
          id_usuario INTEGER,
          id_veiculo INTEGER,
          FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario),
          FOREIGN KEY (id_veiculo) REFERENCES VEICULO(id_veiculo)
        );
      """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS SOLICITACAO_GUINCHO (
          id_solicitacao_guincho INTEGER PRIMARY KEY,
          descricao_solicitacao_guincho TEXT(25),
          id_localizacao INTEGER,
          id_usuario INTEGER,
          id_veiculo INTEGER,
          FOREIGN KEY (id_localizacao) REFERENCES LOCALIZACAO(id_localizacao),
          FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario),
          FOREIGN KEY (id_veiculo) REFERENCES VEICULO(id_veiculo)
        );
      """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS SITUACAO_SOLICITACAO_GUINCHO (
          id_situacao_solicitacao INTEGER PRIMARY KEY,
          id_solicitacao_guincho INTEGER,
          id_guincho INTEGER,
          id_prestador_servico INTEGER,
          FOREIGN KEY (id_solicitacao_guincho) REFERENCES SOLICITACAO_GUINCHO(id_solicitacao_guincho),
          FOREIGN KEY (id_guincho) REFERENCES GUINCHO(id_guincho),
          FOREIGN KEY (id_prestador_servico) REFERENCES PRESTADOR_SERVICO(id_prestador_servico)
        );
      """
    )
    conn.commit()
    return conn


def inserir_usuario(conn, cpf, nome, email, senha, dt_nasc):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO USUARIO (cpf_usuario, nome_usuario, email_usuario, senha_usuario, dt_nasc_usuario) VALUES (?, ?, ?, ?, ?)",
        (cpf, nome, email, senha, dt_nasc),
    )
    conn.commit()


def listar_usuarios(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USUARIO")
    usuarios = cursor.fetchall()
    return usuarios


def atualizar_usuario(conn, id_usuario, cpf, nome, email, senha, dt_nasc):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE USUARIO SET cpf_usuario=?, nome_usuario=?, email_usuario=?, senha_usuario=?, dt_nasc_usuario=? WHERE id_usuario=?",
        (cpf, nome, email, senha, dt_nasc, id_usuario),
    )
    conn.commit()


def excluir_usuario(conn, id_usuario):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM USUARIO WHERE id_usuario=?", (id_usuario,))
    conn.commit()


def inserir_guincho(conn, peso, tipo, disponibilidade):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO GUINCHO (peso_guincho, tipo_guincho, disponibilidade_guincho) VALUES (?, ?, ?)",
        (peso, tipo, disponibilidade),
    )
    conn.commit()


def listar_guinchos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GUINCHO")
    guinchos = cursor.fetchall()
    return guinchos


def atualizar_guincho(conn, id_guincho, peso, tipo, disponibilidade):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE GUINCHO SET peso_guincho=?, tipo_guincho=?, disponibilidade_guincho=? WHERE id_guincho=?",
        (peso, tipo, disponibilidade, id_guincho),
    )
    conn.commit()


def excluir_guincho(conn, id_guincho):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM GUINCHO WHERE id_guincho=?", (id_guincho,))
    conn.commit()


def inserir_endereco(
    conn, cep, rua, num, logradouro, bairro, cidade, municipio, uf, pais
):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ENDERECO (cep_endereco, rua_endereco, num_endereco, logradouro_endereco, bairro_endereco, cidade_endereco, municipio_endereco, uf_endereco, pais_endereco) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (cep, rua, num, logradouro, bairro, cidade, municipio, uf, pais),
    )
    conn.commit()


def listar_enderecos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ENDERECO")
    enderecos = cursor.fetchall()
    return enderecos


def atualizar_endereco(
    conn, id_endereco, cep, rua, num, logradouro, bairro, cidade, municipio, uf, pais
):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE ENDERECO SET cep_endereco=?, rua_endereco=?, num_endereco=?, logradouro_endereco=?, bairro_endereco=?, cidade_endereco=?, municipio_endereco=?, uf_endereco=?, pais_endereco=? WHERE id_endereco=?",
        (cep, rua, num, logradouro, bairro, cidade, municipio, uf, pais, id_endereco),
    )
    conn.commit()


def excluir_endereco(conn, id_endereco):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ENDERECO WHERE id_endereco=?", (id_endereco,))
    conn.commit()


def inserir_prestador_servico(conn, cpf, nome, servico_oferecido):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO PRESTADOR_SERVICO (cpf_prestador_servico, nome_prestador_servico, servico_oferecido_prestador) VALUES (?, ?, ?)",
        (cpf, nome, servico_oferecido),
    )
    conn.commit()


def listar_prestadores_servico(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PRESTADOR_SERVICO")
    prestadores = cursor.fetchall()
    return prestadores


def atualizar_prestador_servico(
    conn, id_prestador_servico, cpf, nome, servico_oferecido
):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE PRESTADOR_SERVICO SET cpf_prestador_servico=?, nome_prestador_servico=?, servico_oferecido_prestador=? WHERE id_prestador_servico=?",
        (cpf, nome, servico_oferecido, id_prestador_servico),
    )
    conn.commit()


def excluir_prestador_servico(conn, id_prestador_servico):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM PRESTADOR_SERVICO WHERE id_prestador_servico=?",
        (id_prestador_servico,),
    )
    conn.commit()


def inserir_tipo_veiculo(conn, nome_tipo_veiculo):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO TIPO_VEICULO (nome_tipo_veiculo) VALUES (?)", (nome_tipo_veiculo,)
    )
    conn.commit()


def listar_tipos_veiculo(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TIPO_VEICULO")
    tipos = cursor.fetchall()
    return tipos


def atualizar_tipo_veiculo(conn, id_tipo_veiculo, nome_tipo_veiculo):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE TIPO_VEICULO SET nome_tipo_veiculo=? WHERE id_tipo_veiculo=?",
        (nome_tipo_veiculo, id_tipo_veiculo),
    )
    conn.commit()


def excluir_tipo_veiculo(conn, id_tipo_veiculo):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM TIPO_VEICULO WHERE id_tipo_veiculo=?", (id_tipo_veiculo,)
    )
    conn.commit()


def inserir_veiculo(
    conn,
    placa_veiculo,
    peso_veiculo,
    comprimento_veiculo,
    altura_veiculo,
    modelo_veiculo,
    chassiAlongado_veiculo,
    qtdEixos_veiculo,
    capacidadeCarga_veiculo,
    disponibilidade_veiculo,
    id_tipoVeiculo_veiculo,
):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO VEICULO (placa_veiculo, peso_veiculo, comprimento_veiculo, altura_veiculo, modelo_veiculo, chassiAlongado_veiculo, qtdEixos_veiculo, capacidadeCarga_veiculo, disponibilidade_veiculo, id_tipoVeiculo_veiculo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            placa_veiculo,
            peso_veiculo,
            comprimento_veiculo,
            altura_veiculo,
            modelo_veiculo,
            chassiAlongado_veiculo,
            qtdEixos_veiculo,
            capacidadeCarga_veiculo,
            disponibilidade_veiculo,
            id_tipoVeiculo_veiculo,
        ),
    )
    conn.commit()


def listar_veiculos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM VEICULO")
    veiculos = cursor.fetchall()
    return veiculos


def atualizar_veiculo(
    conn,
    id_veiculo,
    placa_veiculo,
    peso_veiculo,
    comprimento_veiculo,
    altura_veiculo,
    modelo_veiculo,
    chassiAlongado_veiculo,
    qtdEixos_veiculo,
    capacidadeCarga_veiculo,
    disponibilidade_veiculo,
    id_tipoVeiculo_veiculo,
):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE VEICULO SET placa_veiculo=?, peso_veiculo=?, comprimento_veiculo=?, altura_veiculo=?, modelo_veiculo=?, chassiAlongado_veiculo=?, qtdEixos_veiculo=?, capacidadeCarga_veiculo=?, disponibilidade_veiculo=?, id_tipoVeiculo_veiculo=? WHERE id_veiculo=?",
        (
            placa_veiculo,
            peso_veiculo,
            comprimento_veiculo,
            altura_veiculo,
            modelo_veiculo,
            chassiAlongado_veiculo,
            qtdEixos_veiculo,
            capacidadeCarga_veiculo,
            disponibilidade_veiculo,
            id_tipoVeiculo_veiculo,
            id_veiculo,
        ),
    )
    conn.commit()


def excluir_veiculo(conn, id_veiculo):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM VEICULO WHERE id_veiculo=?", (id_veiculo,))
    conn.commit()


def inserir_localizacao(conn, tipo_terreno_localizacao, desc_localizacao, id_endereco):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO LOCALIZACAO (tipo_terreno_localizacao, desc_localizacao, id_endereco) VALUES (?, ?, ?)",
        (tipo_terreno_localizacao, desc_localizacao, id_endereco),
    )
    conn.commit()


def listar_localizacoes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM LOCALIZACAO")
    localizacoes = cursor.fetchall()
    return localizacoes


def atualizar_localizacao(
    conn, id_localizacao, tipo_terreno_localizacao, desc_localizacao, id_endereco
):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE LOCALIZACAO SET tipo_terreno_localizacao=?, desc_localizacao=?, id_endereco=? WHERE id_localizacao=?",
        (tipo_terreno_localizacao, desc_localizacao, id_endereco, id_localizacao),
    )
    conn.commit()


def excluir_localizacao(conn, id_localizacao):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM LOCALIZACAO WHERE id_localizacao=?", (id_localizacao,))
    conn.commit()


def inserir_seguro(
    conn,
    data_inicio_seguro,
    data_termino_seguro,
    valor_cobertura_seguro,
    id_usuario,
    id_veiculo,
):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO SEGURO (data_inicio_seguro, data_termino_seguro, valor_cobertura_seguro, id_usuario, id_veiculo) VALUES (?, ?, ?, ?, ?)",
        (
            data_inicio_seguro,
            data_termino_seguro,
            valor_cobertura_seguro,
            id_usuario,
            id_veiculo,
        ),
    )
    conn.commit()


def listar_seguros(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SEGURO")
    seguros = cursor.fetchall()
    return seguros


def atualizar_seguro(
    conn,
    id_Seguro,
    data_inicio_seguro,
    data_termino_seguro,
    valor_cobertura_seguro,
    id_usuario,
    id_veiculo,
):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE SEGURO SET data_inicio_seguro=?, data_termino_seguro=?, valor_cobertura_seguro=?, id_usuario=?, id_veiculo=? WHERE id_Seguro=?",
        (
            data_inicio_seguro,
            data_termino_seguro,
            valor_cobertura_seguro,
            id_usuario,
            id_veiculo,
            id_Seguro,
        ),
    )
    conn.commit()


def excluir_seguro(conn, id_Seguro):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM SEGURO WHERE id_Seguro=?", (id_Seguro,))
    conn.commit()


def inserir_solicitacao_guincho(
    conn, descricao_solicitacao_guincho, id_localizacao, id_usuario, id_veiculo
):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO SOLICITACAO_GUINCHO (descricao_solicitacao_guincho, id_localizacao, id_usuario, id_veiculo) VALUES (?, ?, ?, ?)",
        (descricao_solicitacao_guincho, id_localizacao, id_usuario, id_veiculo),
    )
    conn.commit()


def listar_solicitacoes_guincho(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SOLICITACAO_GUINCHO")
    solicitacoes = cursor.fetchall()
    return solicitacoes


def atualizar_solicitacao_guincho(
    conn,
    id_solicitacao_guincho,
    descricao_solicitacao_guincho,
    id_localizacao,
    id_usuario,
    id_veiculo,
):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE SOLICITACAO_GUINCHO SET descricao_solicitacao_guincho=?, id_localizacao=?, id_usuario=?, id_veiculo=? WHERE id_solicitacao_guincho=?",
        (
            descricao_solicitacao_guincho,
            id_localizacao,
            id_usuario,
            id_veiculo,
            id_solicitacao_guincho,
        ),
    )
    conn.commit()


def excluir_solicitacao_guincho(conn, id_solicitacao_guincho):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM SOLICITACAO_GUINCHO WHERE id_solicitacao_guincho=?",
        (id_solicitacao_guincho,),
    )
    conn.commit()


def inserir_situacao_solicitacao_guincho(
    conn, id_solicitacao_guincho, id_guincho, id_prestador_servico
):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO SITUACAO_SOLICITACAO_GUINCHO (id_solicitacao_guincho, id_guincho, id_prestador_servico) VALUES (?, ?, ?)",
        (id_solicitacao_guincho, id_guincho, id_prestador_servico),
    )
    conn.commit()


def listar_situacoes_solicitacao_guincho(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SITUACAO_SOLICITACAO_GUINCHO")
    situacoes = cursor.fetchall()
    return situacoes


def atualizar_situacao_solicitacao_guincho(
    conn,
    id_situacao_solicitacao,
    id_solicitacao_guincho,
    id_guincho,
    id_prestador_servico,
):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE SITUACAO_SOLICITACAO_GUINCHO SET id_solicitacao_guincho=?, id_guincho=?, id_prestador_servico=? WHERE id_situacao_solicitacao=?",
        (
            id_solicitacao_guincho,
            id_guincho,
            id_prestador_servico,
            id_situacao_solicitacao,
        ),
    )
    conn.commit()


def excluir_situacao_solicitacao_guincho(conn, id_situacao_solicitacao):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM SITUACAO_SOLICITACAO_GUINCHO WHERE id_situacao_solicitacao=?",
        (id_situacao_solicitacao,),
    )
    conn.commit()
