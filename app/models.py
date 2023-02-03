from app import db
from werkzeug.security import generate_password_hash


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String, nullable=False)

    def __init__(self, json):
        self.nome_usuario = json.get('usuario')
        self.email = json.get('email')
        self.senha = generate_password_hash(json.get('senha'))

    def usuario_valido(self):
        valido = False
        if self.nome_usuario and self.email and self.senha:
            valido = True
        return valido

    def to_json(self, cont):
        return {
            'contador': cont,
            'nome_usuario': self.nome_usuario,
            'email': self.email,
            'id': self.id
        }