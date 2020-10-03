# Technical Challenge - Editora Globo
A **Python Flask** CRUD API for **Artists, Album and Track** datas. It also consumes **Deezer API** to populate database. 
Developed by **Ygohr Medeiros** for technical challenge of **Editora Globo**.
 
## -> Technologies
This project uses **Python with Flask** for the backend, and **MySQL** for the database storage.

## -> Dependecies:
To run the project you'll need to have installed:
 - Flask==1.1.2
 - Flask-SQLAlchemy==2.4.4
 - SQLAlchemy==1.3.19
 - gunicorn==19.9.0**
 
## -> Host - Heroku App
The API can be accessed by **Heroku APP** -> https://desafio-editora-globo-ygohr.herokuapp.com/

## -> How to
The API have some routes that can receive parameters by **URL or by JSON**, this last one to create and update data.

### Routes / Parameters:
/consultaArtistaDeezer -> Receive an id to consult data from Deezer API and insert to database. (Example: /consultaArtistaDeezer?id=14)

/consultaAlbumDeezer -> Receive an id to consult data from Deezer API and insert to database. (Example: /consultaAlbumDeezer?id=302127)

/consultaMusicaDeezer -> Receive an id to consult data from Deezer API and insert to database. (Example: /consultaMusicaDeezer?id=3135556)

/cadastrarArtista -> Use a JSON to insert data. Can be accessed by POST requests in Insomnia/Postman. (Use Insomnia_Requests_Desafio_Globo.json file)

/excluirArtista -> Receive an id to remove "artista" data. (Example: /excluirArtista?id=14)

/atualizarArtista -> Use a JSON to update data. Can be accessed by POST requests in Insomnia/Postman. (Use Insomnia_Requests_Desafio_Globo.json file)

/listaArtista -> Can receive an id to consult a especific data from database or use "/" to consult all datas. (Example: /listaArtista?id=14 | /listaArtista)

/cadastrarAlbum -> Use a JSON to insert data. Can be accessed by POST requests in Insomnia/Postman. (Use Insomnia_Requests_Desafio_Globo.json file)

/excluirAlbum -> Receive an id to remove data. (Example: /excluirAlbum?id=14)

/atualizarAlbum -> Use a JSON to insert data. Can be accessed by POST requests in Insomnia/Postman. (Use Insomnia_Requests_Desafio_Globo.json file)

/listaAlbum -> Can receive an id or idArtista to consult a especific data from database or use "/" to consult all datas. (Example: /listaAlbum?id=14 | /listaAlbum | /listaAlbum?artista=14)

/cadastrarMusica -> Use a JSON to insert data. Can be accessed by POST requests in Insomnia/Postman. (Use Insomnia_Requests_Desafio_Globo.json file)

/excluirMusica -> Receive an id to remove data. (Example: /excluirMusica?id=14)

/atualizarMusica -> Use a JSON to insert data. Can be accessed by POST requests in Insomnia/Postman. (Use Insomnia_Requests_Desafio_Globo.json file)

/listaMusica -> Can receive an id or idAlbum to consult a especific data from database or use "/" to consult all datas. (Example: /listaMusica?id=14 | /listaMusica | /listaMusica?artista=14)
