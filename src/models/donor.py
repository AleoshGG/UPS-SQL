# Importamos las dependencias
from src.models.donee import Donee
from sqlalchemy.dialects.postgresql import ENUM
from dotenv import load_dotenv
from . import db
import os
load_dotenv()

# Definición de la clase donatarios
class Donor(Donee):

    schema_name = os.getenv("SCHEMA")
    __tablename__ = 'donors'
    __table_args__ = {'schema': schema_name}

    id_donor = db.Column(db.Integer, primary_key=True, auto_increment= True)
    health_status = db.Column(ENUM('good', 'recovery', name="health_status_enum"), nullable=False)
    availability = db.Column(ENUM('morning', 'afternoon', name="availability_enum"), nullable=False)
    blood_type = db.Column(ENUM(
        'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-',
        name="blood_type_enum"), nullable=False, unique=True)
    donations_number = db.Column(db.Integer, nullable = False)
    last_donation = db.Column(db.Date, nullable = False)

    def __init__(self, first_name, last_name, email, password, phone_number, health_status, availability, donations_number, last_donation, address=None):
        super.__init__(first_name, last_name, email, password, phone_number, address)
        self.health_status = health_status
        self.availability = availability
        self.donations_number = donations_number
        self.last_donation = last_donation

    def __repr__(self):
        return f'<User {self.id_donor}>'