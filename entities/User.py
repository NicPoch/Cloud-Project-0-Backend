from app_imports import db

class User(db.Model):

    __tablename__='user'

    id=db.Column(db.Integer,primary_key=True)
    mail=db.Column(db.Text,nullable=False,unique=True)
    password=db.Column(db.Text,nullable=False)
    eventos=db.relationship("Evento",backref='user',lazy='dynamic',cascade="all, delete")

    @property
    def serialize(self): 
        return {'id':self.id,'mail':self.mail,'password':self.password} 