#coding:utf-8
from flask import request, url_for, redirect, jsonify, json
from models.artista import *
from models.album import *
from models.musica import *

import requests

from db import *

db.create_all()

deezer_artist_url_base = "https://api.deezer.com/artist/"
deezer_album_url_base = "https://api.deezer.com/album/"
deezer_music_url_base = "https://api.deezer.com/track/"

@app.route("/")
def index():
    return ("<strong>Nesta API existem as seguintes rotas:</strong> <br>"
                   "/consultaArtistaDeezer <br>"
                   "/consultaAlbumDeezer <br>"
                   "/consultaMusicaDeezer <br>"
                   "/cadastrarArtista <br>"
                   "/excluirArtista <br>"
                   "/atualizarArtista <br>"
                   "/listaArtista <br>"
                   "/cadastrarAlbum <br>"
                   "/excluirAlbum <br>"
                   "/atualizarAlbum <br>"
                   "/listaAlbum <br>"
                   "/cadastrarMusica <br>"
                   "/excluirMusica <br>"
                   "/atualizarMusica <br>"
                   "/listaMusica <br><br>"
                   "Acesse alguma dessas rotas para começar a usar!"
    )

@app.route("/consultaArtistaDeezer")
def consultaArtistaDeezer():

    if not request.args:
        return jsonify("Digite o id de um artista para consultar e cadastrar através do Deezer")

    artista = request.args["id"]
    response = requests.get(deezer_artist_url_base + "" + artista)
    jsonData = response.json()
    nomeArtista = jsonData['name']

    inserirArtista = Artista(nomeArtista)
    db.session.add(inserirArtista)
    db.session.commit()

    return redirect(url_for("listaArtista"))

@app.route("/consultaAlbumDeezer")
def consultaAlbumDeezer():

    if not request.args:
        return jsonify("Digite o id de um album para consultar e cadastrar através do Deezer")

    album = request.args["id"]
    response = requests.get(deezer_album_url_base + "" + album)
    jsonData = response.json()
    nomeAlbum = jsonData['title']
    jsonDataArtista = jsonData['artist']
    idArtista = jsonDataArtista.get('id')

    inserirAlbum = Album(nomeAlbum, idArtista)
    db.session.add(inserirAlbum)
    db.session.commit()

    return redirect(url_for("listaAlbum"))


@app.route("/consultaMusicaDeezer")
def consultaMusicaDeezer():

    if not request.args:
        return jsonify("Digite o id de uma musica para consultar e cadastrar através do Deezer")

    musica = request.args["id"]
    response = requests.get(deezer_music_url_base + "" + musica)
    jsonData = response.json()

    nomeMusica = jsonData['title']
    jsonDataAlbum = jsonData['album']
    idAlbum = jsonDataAlbum.get('id')

    inserirMusica = Musica(nomeMusica, idAlbum)
    db.session.add(inserirMusica)
    db.session.commit()

    return redirect(url_for("listaMusica"))

# BLOCO DE DADOS ARTISTAS #
@app.route("/cadastrarArtista", methods=['GET', 'POST'])
def cadastrarArtista():

    parametro = '"' + str(request.json) + '"'
    dados = json.loads(parametro)
    validador = "nome" in dados

    if not validador:
        return jsonify("Preencha os dados do json corretamente")
    else:
        nome = request.json["nome"]
        artista = Artista(nome)
        db.session.add(artista)
        db.session.commit()
        return redirect(url_for("listaArtista"))

@app.route("/excluirArtista")
def excluirArtista():

    if not request.args:
        return jsonify("Digite o id de um registro para excluir")

    id = request.args["id"]
    artista = Artista.query.filter_by(_id=id).first()

    if not artista:
        return jsonify("Artista inexistente")
    else:
        db.session.delete(artista)
        db.session.commit()

        return redirect(url_for("listaArtista"))

@app.route("/atualizarArtista", methods=['GET', 'POST'])
def atualizarArtista():

    parametro = '"' + str(request.json) + '"'
    dados = json.loads(parametro)
    validaID = "id" in dados
    validaNome = "nome" in dados


    if not validaID or not validaNome:
        return jsonify("Preencha os dados do json corretamente")

    id = request.json["id"]

    artista = Artista.query.filter_by(_id=id).first()

    if artista:
        nome = request.json["nome"]
        artista.nome = nome
        db.session.commit()

        return redirect(url_for("listaArtista"))
    else:
        return jsonify("Artista inexiste")

@app.route("/listaArtista", methods=['GET', 'POST'])
def listaArtista():

    if not request.args:
        listReturn = []
        artistas = Artista.query.all()

        for artista in artistas:
            listReturn.append(artista.returnData())

        return jsonify(listReturn)
    else:
        id = request.args["id"]
        artista = Artista.query.filter_by(_id=id).first()

        return jsonify(artista.returnData()) if artista != None else jsonify("Não há registro para o filtro realizado")

# FIM BLOCO - ARTISTAS #

# BLOCO DE DADOS ALBUM #
@app.route("/cadastrarAlbum", methods=['GET', 'POST'])
def cadastrarAlbum():

    parametro = '"' + str(request.json) + '"'
    dados = json.loads(parametro)
    validadorNome = "nome" in dados
    validadorIdArtista = "idArtista" in dados

    if not validadorNome or not validadorIdArtista:
        return jsonify("Preencha os dados do json corretamente")
    else:
        nome = request.json["nome"]
        idArtista = request.json["idArtista"]
        album = Album(nome, idArtista)
        db.session.add(album)
        db.session.commit()
        return redirect(url_for("listaAlbum"))

@app.route("/excluirAlbum")
def excluirAlbum():

    if not request.args:
        return jsonify("Digite o id de um registro para excluir")

    id = request.args["id"]
    album = Album.query.filter_by(_id=id).first()

    if not album:
        return jsonify("Album inexistente")
    else:
        db.session.delete(album)
        db.session.commit()

        return redirect(url_for("listaAlbum"))

@app.route("/atualizarAlbum", methods=['GET', 'POST'])
def atualizarAlbum():

    parametro = '"' + str(request.json) + '"'
    dados = json.loads(parametro)
    validaID = "id" in dados
    validaNome = "nome" in dados
    validaIDArtista = "idArtista" in dados

    if not validaID or not validaNome or not validaIDArtista:
        return jsonify("Preencha os dados do json corretamente")

    id = request.json["id"]
    nome = request.json["nome"]
    idArtista = request.json["idArtista"]
    album = Album.query.filter_by(_id=id).first()

    if album:
        album.nome = nome
        album.idArtista = idArtista

        db.session.commit()

        return redirect(url_for("listaAlbum"))
    else:
        return jsonify("Artista inexiste")

@app.route("/listaAlbum", methods=['GET', 'POST'])
def listaAlbum():

    parametro = '"' + str(request.args) + '"'
    dados = json.loads(parametro)
    validaID = "id" in dados
    validaIDArtista = "artista" in dados
    listReturn = []

    if not request.args:

        albuns = Album.query.all()

        for album in albuns:
            listReturn.append(album.returnData())

        return jsonify(listReturn)
    else:
        if validaID:
            id = request.args["id"]
            album = Album.query.filter_by(_id=id).first()

            if album is not None:
                listReturn.append(album.returnData())
            else:
                listReturn.append({
                    "resultado": "Não há registro para o filtro realizado"
                })
        elif validaIDArtista:
            idArtista = request.args["artista"]
            albuns = Album.query.filter_by(idArtista=idArtista).all()

            if len(albuns) > 0:
                for album in albuns:
                    listReturn.append(album.returnData())
            else:
                listReturn.append({
                    "resultado": "Não há registro para o filtro realizado"
                })

    return jsonify(listReturn)

#### FIM BLOCO - ALBUM ####

#### BLOCO DE DADOS MUSICA ####
@app.route("/cadastrarMusica", methods=['GET', 'POST'])
def cadastrarMusica():

    parametro = '"' + str(request.json) + '"'
    dados = json.loads(parametro)
    validadorNome = "nome" in dados
    validadorIdAlbum = "idAlbum" in dados

    if not validadorNome or not validadorIdAlbum:
        return jsonify("Preencha os dados do json corretamente")
    else:
        nome = request.json["nome"]
        idAlbum = request.json["idAlbum"]
        musica = Musica(nome, idAlbum)
        db.session.add(musica)
        db.session.commit()
        return redirect(url_for("listaMusica"))

@app.route("/excluirMusica")
def excluirMusica():

    if not request.args:
        return jsonify("Digite o id de um registro para excluir")

    id = request.args["id"]
    musica = Musica.query.filter_by(_id=id).first()

    if not musica:
        return jsonify("Musica inexistente")
    else:
        db.session.delete(musica)
        db.session.commit()

        return redirect(url_for("listaMusica"))

@app.route("/atualizarMusica", methods=['GET', 'POST'])
def atualizarMusica():

    parametro = '"' + str(request.json) + '"'
    dados = json.loads(parametro)
    validaID = "id" in dados
    validaNome = "nome" in dados
    validaIDAlbum = "idAlbum" in dados

    if not validaID or not validaNome or not validaIDAlbum:
        return jsonify("Preencha os dados do json corretamente")

    id = request.json["id"]
    nome = request.json["nome"]
    idAlbum = request.json["idAlbum"]
    musica = Musica.query.filter_by(_id=id).first()

    if musica:
        musica.nome = nome
        musica.idAlbum = idAlbum

        db.session.commit()

        return redirect(url_for("listaMusica"))
    else:
        return jsonify("Musica inexiste")

@app.route("/listaMusica", methods=['GET', 'POST'])
def listaMusica():
    listReturn = []
    parametro = '"' + str(request.args) + '"'
    dados = json.loads(parametro)
    validaID = "id" in dados
    validaIDAlbum = "album" in dados

    if not request.args:

        musicas = Musica.query.all()

        for musica in musicas:
            listReturn.append(musica.returnData())

        return jsonify(listReturn)
    else:
        if validaID:
            id = request.args["id"]
            musica = Musica.query.filter_by(_id=id).first()

            if musica is not None:
                listReturn.append(musica.returnData())
            else:
                listReturn.append({
                    "resultado": "Não há registro para o filtro realizado"
                })

        elif validaIDAlbum:
            idAlbum = request.args["album"]
            musicas = Musica.query.filter_by(idAlbum=idAlbum).all()

            if len(musicas) > 0:
                for musica in musicas:
                    listReturn.append(musica.returnData())
            else:
                listReturn.append({
                    "resultado": "Não há registro para o filtro realizado"
                })

    return jsonify(listReturn)

if __name__ == "__main__":
    app.run(debug=True)