from entities.Evento import Evento
from app_imports import db

def create(nombre,categoria,lugar,direccion,inicio,fin,presencial,creador):
    new_evento=Evento(nombre=nombre,categoria=categoria,lugar=lugar,direccion=direccion,inicio=inicio,fin=fin,presencial=presencial,creador=creador)
    db.session.add(new_evento)
    db.session.commit()
    print(new_evento)
    return new_evento
def find(id)->Evento:
    evento=Evento.query.get(id)
    if evento==None:
        raise Exception(f'Evento doesn\'t exist with id {id}')
    return evento
def findUser(id):
    eventos=Evento.query.filter_by(creador=id).all()
    return eventos
def update(id,nombre,categoria,lugar,direccion,inicio,fin,presencial):
    evento=Evento.query.get(id)
    if evento==None:
        raise Exception(f'Evento doesn\'t exist with id {id}')
    evento.nombre=nombre
    evento.categoria=categoria
    evento.lugar=lugar
    evento.direccion=direccion
    evento.inicio=inicio
    evento.fin=fin
    evento.presencial=presencial
    db.session.commit()
    return evento
def delete(id):
    evento=Evento.query.get(id)
    if evento==None:
        raise Exception(f'Evento doesn\'t exist with id {id}')
    db.session.delete(evento)
    db.session.commit()
    return evento