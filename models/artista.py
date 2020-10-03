from db import *

class Artista(db.Model):
    __tablename__ = 'artista'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))

    def __init__(self, nome):
        self.nome = nome

    def returnData(self):
        dict = {
            "id": self._id,
            "nome": self.nome
        }

        return dict