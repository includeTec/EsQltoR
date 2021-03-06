# -*- coding: utf-8 -*-
# Controlador de la Lista de Escultores.
def index():
    artistas = db().select(db.t_artistas.ALL,orderby=db.t_artistas.id)
    titulo="Artistas"
    return dict(artistas=artistas, titulo=titulo)

def show():
    artista = db.t_artistas(request.args(0)) or redirect(URL('index'))
    titulo="Artista"
    return dict(artista=artista, titulo=titulo)

def download():
    return response.download(request, db)

def escultura():
    titulo="Escultura"
    artista = db.t_artistas(request.args(0)) or redirect(URL('index'))
    escultura = db(db.t_esculturas.f_escultura_id==artista.f_artista_nombre).select().first()
   
    return dict(artista=artista, escultura=escultura, titulo=titulo)
