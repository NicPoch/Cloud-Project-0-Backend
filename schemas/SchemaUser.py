from app_imports import ma
from entities.User import User

class User_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=User
        fields=("id","mail")