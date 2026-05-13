from flask import Blueprint, request
from controllers.jogo_controllers import get_jogos, create_jogo, get_jogo_by_id

# Define um Blueprint para as rotas de "Jogo"
jogo_routes = Blueprint('jogo_routes', __name__)

# Rota para listar todos os jogos (GET)
@jogo_routes.route('/Jogo', methods=['GET'])
def jogos_get():
    return get_jogos()

# Rota para buscar um jogo pelo ID (GET)
@jogo_routes.route('/Jogo/<int:jogo_id>', methods=['GET'])
def jogo_get_by_id(jogo_id):
    return get_jogo_by_id(jogo_id)

# Rota para criar um novo jogo (POST)
@jogo_routes.route('/Jogo', methods=['POST'])
def jogos_post():
    return create_jogo(request.json)