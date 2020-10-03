from db import *

class Musica(db.Model):
    __tablename__ = 'musica'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    idAlbum = db.Column(db.Integer)

    def __init__(self, nome, idAlbum):
        self.nome = nome,
        self.idAlbum = idAlbum

    def returnData(self):
        dict = {
            "id": self._id,
            "nome": self.nome,
            "idAlbum": self.idAlbum
        }

        return dict