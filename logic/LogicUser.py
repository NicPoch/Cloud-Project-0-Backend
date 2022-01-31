from persistence.PersistenceUser import *
from schemas.SchemaUser import User_Schema
import traceback

user_schema=User_Schema()

def createUser(req):
    if "mail" not in req:
        return 'No mail provided',404
    if "password" not in req:
        return 'No password provided',404
    try:
        return user_schema.dump(create(req["mail"],req["password"]))
    except Exception as e:
        traceback.print_exc()
        return str(e),505
def findUser(id):
    try:
        return user_schema.dump(find(id))
    except Exception as e:
        traceback.print_exc()
        return str(e),404
def login(req):
    if "mail" not in req:
        return 'No mail provided',404
    if "password" not in req:
        return 'No password provided',404
    try:
        return user_schema.dump(findByLogin(req["mail"],req["password"]))
    except Exception as e:
        traceback.print_exc()
        return str(e),404
def updateUser(id,req):
    if "password" not in req:
        return 'No password provided',404
    try:
        return user_schema.dump(update(id,req["password"]))
    except Exception as e:
        traceback.print_exc()
        return str(e),404
def deleteUser(id):
    try:
        return user_schema.dump(delete(id))
    except Exception as e:
        traceback.print_exc()
        return str(e),404