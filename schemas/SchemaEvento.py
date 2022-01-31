from app_imports import ma

class Evento_Schema(ma.Schema):
    class Meta:
        fields=("id","nombre","categoria","lugar","direccion","inicio","fin","presencial","creador")