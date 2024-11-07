# Importación de dependencias
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from sqlalchemy.dialects.postgresql import ENUM
import os
from . import db
bcrypt = Bcrypt()
load_dotenv()  

# Definición de la clase donatarios
class Contributions(db.Model):

    schema_name = os.getenv("SCHEMA")
    __tablename__ = 'profile'
    __table_args__ = {'schema': schema_name}

    id_donor = db.Column(db.Integer, db.ForeignKey('donors.id_donor'), primary_key=True)
    id_donee = db.Column(db.Integer, db.ForeignKey('donees.id_donee'), primary_key=True)

    def __init__(self, id_donor, id_donee):
        if not isinstance(id_donor, int) or not isinstance(id_donee, int):
            raise ValueError("Both id_donor and id_donee must be integers.")
        self.id_donor = id_donor
        self.id_donee = id_donee

    def __repr__(self):
        return f"<Contributions(id_donor={self.id_donor}, id_donee={self.id_donee})>"
