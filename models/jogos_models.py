# Importa o objeto db de 'db', que fornece as funcionalidades do SQLAlchemy para interagir com o banco de dados
from db import db

# Define a classe Jogo que representa a tabela 'jogos' no banco de dados
class Jogo(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'jogos'

    # Define as colunas da tabela 'jogos'
    id = db.Column(db.Integer, primary_key=True)  # Coluna para o ID do jogo, chave primária
    titulo = db.Column(db.String(80), nullable=False)  # Coluna para o título do jogo
    genero = db.Column(db.String(80), nullable=False)  # Coluna para o gênero do jogo
    desenvolvedor = db.Column(db.String(80), nullable=False)  # Coluna para o desenvolvedor
    plataforma = db.Column(db.String(80), nullable=False)  # Coluna para a plataforma

    # Método para retornar os dados do jogo como um dicionário
    def json(self):
        return {
            'id': self.id,  # ID do jogo
            'titulo': self.titulo,  # Título do jogo
            'genero': self.genero,  # Gênero do jogo
            'desenvolvedor': self.desenvolvedor,  # Desenvolvedor do jogo
            'plataforma': self.plataforma  # Plataforma do jogo
        }
