from db import *

class Album(db.Model):
    __tablename__ = 'album'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    idArtista = db.Column(db.Integer)

    def __init__(self, nome, idArtista):
        self.nome = nome,
        self.idArtista = idArtista

    def returnData(self):
        dict = {
            "id": self._id,
            "nome": self.nome,
            "idArtista": self.idArtista
        }

        return dict