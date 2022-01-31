from flask import Flask
from flask_restful import Api

from resources.ResourceEvento import ResourceEvento,ResourceEventos,ResourceUserEventos
from resources.ResourceUser import ResourceLogin,ResourceUsers,ResourceUser


app=Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database.db'


api=Api(app)

@app.before_request
def create_tables():
    db.create_all()

api.add_resource(ResourceUsers,'/users')
api.add_resource(ResourceUser,'/users/<int:id>')
api.add_resource(ResourceLogin,'/login')

api.add_resource(ResourceEvento,'/eventos/<int:id>')
api.add_resource(ResourceEventos,'/eventos')
api.add_resource(ResourceUserEventos,'/eventos/user/<int:id>')


if __name__=="__main__":
    from app_imports import ma,db
    db.init_app(app)
    ma.init_app(app)
    app.debug=True
    app.run()    