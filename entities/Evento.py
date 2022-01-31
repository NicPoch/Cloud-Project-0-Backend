from app_imports import db

class Evento(db.Model):

    __tablename__='evento'

    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.Text,nullable=False)
    categoria=db.Column(db.Text,nullable=False)
    lugar=db.Column(db.Text,nullable=False)
    direccion=db.Column(db.Text,nullable=False)
    inicio=db.Column(db.DateTime,nullable=False)
    fin=db.Column(db.DateTime,nullable=False)
    presencial=db.Column(db.Boolean,nullable=False)
    creador=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    @property
    def serialize(self):
        return {'id':self.id,'nombre':self.nombre,'categoria':self.categoria,'lugar':self.lugar,
            'direccion':self.direccion,'inicio':self.inicio.strftime("%d/%m/%Y"),
            'fin':self.fin.strftime("%d/%m/%Y"),'presencial':self.presencial,'creador':self.creador}   