from src.models.address import Address
from flask_bcrypt import Bcrypt
from . import db
import os
from dotenv import load_dotenv
bcrypt = Bcrypt()
load_dotenv()

class Donee(db.Model):

    schema_name = os.getenv("SCHEMA")
    __tablename__ = 'donees'
    __table_args__ = {'schema': schema_name}

    id_donee = db.Column(db.Integer, primary_key=True, autoincrement = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    address = db.Column(Address)
    email = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(50), nullable = False)
    phone_number = db.Column(db.String(10), nullable = False)

    def __init__(self, first_name, last_name, email, password, phone_number, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.address = address
        self.phone_number = phone_number
        print(self.first_name, self.last_name, self.email, self.password, self.phone_number)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
     
    def set_address(self, address):
        print(address)
        if isinstance(address, dict) and all(key in address for key in ["state", "locality", "distrit", "postal_code"]):
            self.address = address
        else:
            raise ValueError("La dirección debe incluir los campos state, locality, distrit y postal_code")
        print(self.address)

    def get_address(self):
        return self.address 
    
    def __repr__(self):
        return f'<User {self.nombre}>'