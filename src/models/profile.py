# Importación de dependencias
from sqlalchemy import ForeignKey
from . import db
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from sqlalchemy.dialects.postgresql import ENUM
import os
bcrypt = Bcrypt()
load_dotenv()  

# Definición de la clase donatarios
class Profile(db.Model):

    schema_name = os.getenv("SCHEMA")
    __tablename__ = 'profile'
    __table_args__ = {'schema': schema_name}

    id_donor = db.Column(db.Integer, ForeignKey(f'{schema_name}.donors.id_donor'), primary_key=True)
    health_status = db.Column(ENUM('Good', 'Recovery', name="health_status_enum"), nullable=False)
    availability = db.Column(ENUM('morning', 'afternoon', name="availability_enum"), nullable=False)
    blood_type = db.Column(ENUM(
        'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-',
        name="blood_type_enum"), nullable=False)
    donations_number = db.Column(db.Integer, nullable=False)
    last_donation = db.Column(db.Date, nullable=False)

    def __init__(self, id_donor, bloodType):
        self.id_donor = id_donor
        self.health_status = 'Good'
        self.availability = 'morning'
        self.donations_number = 0
        self.blood_type = bloodType
        self.last_donation = '2024-01-01'