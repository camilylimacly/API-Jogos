from models.jogo_models import Jogo  # Importa o modelo Jogo
from db import db  # Importa a conexão com o banco de dados
import json
from flask import make_response, request

# Função para obter todos os jogos
def get_jogos():
    jogos = Jogo.query.all()  # Busca todos os jogos no banco de dados

    response = make_response(
        json.dumps({
            'mensagem': 'Lista de jogos.',
            'dados': [jogo.json() for jogo in jogos]  # Converte os objetos de jogo para JSON
        }, ensure_ascii=False, sort_keys=False)
    )

    response.headers['Content-Type'] = 'application/json'
    return response

# Função para obter um jogo específico por ID
def get_jogo_by_id(jogo_id):
    jogo = Jogo.query.get(jogo_id)  # Busca o jogo pelo ID

    if jogo:
        response = make_response(
            json.dumps({
                'mensagem': 'Jogo encontrado.',
                'dados': jogo.json()  # Converte os dados do jogo para JSON
            }, ensure_ascii=False, sort_keys=False)
        )

        response.headers['Content-Type'] = 'application/json'
        return response

    else:
        response = make_response(
            json.dumps({
                'mensagem': 'Jogo não encontrado.',
                'dados': {}
            }, ensure_ascii=False),
            404
        )

        response.headers['Content-Type'] = 'application/json'
        return response

# Função para criar um novo jogo
def create_jogo(jogo_data):

    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in jogo_data for key in ['titulo', 'genero', 'desenvolvedor', 'plataforma']):

        response = make_response(
            json.dumps({
                'mensagem': 'Dados inválidos. Título, gênero, desenvolvedor e plataforma são obrigatórios.'
            }, ensure_ascii=False),
            400
        )

        response.headers['Content-Type'] = 'application/json'
        return response

    # Cria o novo jogo
    novo_jogo = Jogo(
        titulo=jogo_data['titulo'],
        genero=jogo_data['genero'],
        desenvolvedor=jogo_data['desenvolvedor'],
        plataforma=jogo_data['plataforma']
    )

    db.session.add(novo_jogo)  # Adiciona o jogo ao banco
    db.session.commit()  # Salva no banco

    # Retorna resposta de sucesso
    response = make_response(
        json.dumps({
            'mensagem': 'Jogo cadastrado com sucesso.',
            'jogo': novo_jogo.json()
        }, ensure_ascii=False, sort_keys=False)
    )

    response.headers['Content-Type'] = 'application/json'
    return response