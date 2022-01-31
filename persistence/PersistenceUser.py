from entities.User import User
from app_imports import db

def create(mail,password):
    try:
        new_user=User(mail=mail,password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except Exception as e:
        raise e
def find(id):
    user=User.query.get(id)
    if user==None:
        raise Exception(f'User doesn\'t exist with id {id}')
    return user
def findByLogin(mail,password):
    user=User.query.filter_by(mail=mail,password=password).first()
    if user==None:
        raise Exception(f'User doesn\'t exist with login')
    return user
def update(id,password):
    user=User.query.get(id)
    if user==None:
        raise Exception(f'User doesn\'t exist with id {id}')
    user.password=password
    db.session.commit()
    return user
def delete(id):
    user=User.query.get(id)
    if user==None:
        raise Exception(f'User doesn\'t exist with id {id}')
    db.session.delete(user)
    db.session.commit()
    return user