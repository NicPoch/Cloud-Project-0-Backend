from persistence.PersistenceEvento import *
from schemas.SchemaEvento import Evento_Schema
from app_imports import datetime
import traceback

evento_schema=Evento_Schema()
eventos_schema=Evento_Schema(many=True)

valid_categories=['Conferencia','Seminario','Congreso','Curso']

def createEvento(req):
    if "nombre" not in req:
        return 'No nombre',404
    if "categoria" not in req:
        return 'No categoria',404
    if "lugar" not in req:
        return 'No lugar',404
    if "direccion" not in req:
        return 'No direccion',404
    if "inicio" not in req:
        return 'No inicio',404
    if "fin" not in req:
        return 'No fin',404
    if "presencial" not in req:
        return 'No tipo',404
    if "creador" not in req:
        return 'No creador',404
    if len(req["nombre"])==0:
        return 'empty nombre',404
    if req["categoria"] not in valid_categories:
        return 'Invalid categoria',404
    if len(req["lugar"])==0:
        return 'empty lugar',404
    if len(req["direccion"])==0:
        return 'empty direccion',404
    try:
        datetime.strptime(req["inicio"],'%d/%m/%Y')
    except:
        return 'Wrong date format inicio',404
    try:
        datetime.strptime(req["fin"],'%d/%m/%Y')
    except:
        return 'Wrong date format fin',404
    if(datetime.strptime(req["inicio"],'%d/%m/%Y')> datetime.strptime(req["fin"],'%d/%m/%Y')):
        return 'Invaid time',404
    try:
        return evento_schema.dump(create(nombre=req["nombre"],categoria=req["categoria"],
            lugar=req["lugar"],direccion=req["direccion"],inicio=datetime.strptime(req["inicio"],'%d/%m/%Y'),
            fin=datetime.strptime(req["fin"],'%d/%m/%Y'),presencial=req["presencial"],creador=req["creador"])) 
    except Exception as e:
        traceback.print_exc()
        return str(e),505
def findEvento(id):
    try:
        return evento_schema.dump(find(id))
    except Exception as e:
        traceback.print_exc()
        return str(e),505
def findUserEventos(id):
    try:
        return eventos_schema.dump(findUser(id))
    except Exception as e:
        traceback.print_exc()
        return str(e),505
def updateEvento(id,req):
    if "nombre" not in req:
        return 'No nombre',404
    if "categoria" not in req:
        return 'No categoria',404
    if "lugar" not in req:
        return 'No lugar',404
    if "direccion" not in req:
        return 'No direccion',404
    if "inicio" not in req:
        return 'No inicio',404
    if "fin" not in req:
        return 'No fin',404
    if "presencial" not in req:
        return 'No tipo',404
    if len(req["nombre"])==0:
        return 'empty nombre',404
    if req["categoria"] not in valid_categories:
        return 'Invalid categoria',404
    if len(req["lugar"])==0:
        return 'empty lugar',404
    if len(req["direccion"])==0:
        return 'empty direccion',404
    try:
        datetime.strptime(req["inicio"],'%d/%m/%Y')
    except:
        return 'Wrong date format inicio',404
    try:
        datetime.strptime(req["fin"],'%d/%m/%Y')
    except:
        return 'Wrong date format fin',404
    if(datetime.strptime(req["inicio"],'%d/%m/%Y')> datetime.strptime(req["fin"],'%d/%m/%Y')):
        return 'Invaid time',404
    try:
        return evento_schema.dump(update(id,nombre=req["nombre"],categoria=req["categoria"],
            lugar=req["lugar"],direccion=req["direccion"],inicio=datetime.strptime(req["inicio"],'%d/%m/%Y'),
            fin=datetime.strptime(req["fin"],'%d/%m/%Y'),presencial=req["presencial"]))
    except Exception as e:
        traceback.print_exc()
        return str(e),505
def deleteEvento(id):
    try:
        return evento_schema.dump(delete(id))
    except Exception as e:
        traceback.print_exc()
        return str(e),505