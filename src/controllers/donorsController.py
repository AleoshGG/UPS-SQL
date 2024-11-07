from tokenize import String
from typing import cast
from flask import jsonify
from sqlalchemy import func, select, text
from src.models.donor import Donor, db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

def createDonor(data):
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    phone_number = data.get('phone_number')
    address = data.get('address')
    health_status = data.get('health_status')
    availability = data.get('availability')
    donations_number = data.get('donations_number')
    last_donation = data.get('last_donation')
    blood_type = data.get('blood_type')

    try:
        # Obtener los datos
        newDonor = Donor(
            first_name, 
            last_name, 
            email, 
            password, 
            phone_number,
            health_status,
            availability,
            donations_number,
            blood_type=blood_type,
            last_donation=last_donation)
        newDonor.set_address(address)
        # Inserción 
        db.session.add(newDonor)
        db.session.commit()

        # resultado
        return jsonify({
            "msg": "Success",
            "id_donee": newDonor.id_donor
        }), 201
    except Exception as e:
        return jsonify({
            "error": "An unexpected error occurred",
            "details": str(e)
        }), 500

# @jwt_required
# def updateDonee(id_donee, data):
#     try:
#         # Buscar el donatario en la base de datos
#         donee = Donee.query.get(id_donee)

#         if not donee:
#             return jsonify({"error": "Donee not found"}), 404

#         # Actualizar solo los atributos que se proporcionan en el data
#         for key, value in data.items():
#             if hasattr(donee, key):
#                 setattr(donee, key, value)

#         # Guardar los cambios en la base de datos
#         db.session.commit()

#         return jsonify({
#             "msg": "Donee updated successfully",
#             "id_donee": donee.id_donee,
#         }), 200
#     except Exception as e:
#         return jsonify({
#             "error": "An unexpected error occurred",
#             "details": str(e)
#         }), 500

def login_usuario(data):
    email = data.get('email')
    password = data.get('password')

    donor = Donor.query.filter_by(email=email).first()
    if not donor or not donor.check_password(password):
        return jsonify({"mensaje": "Credenciales inválidas"}), 401

    access_token = create_access_token(identity=donor.id_donor)
    return jsonify({"mensaje": "Inicio de sesión exitoso", "token": access_token}), 200
""" 
@jwt_required()
def obtener_usuario():
    Donee_id = get_jwt_identity()
    Donee = Donee.query.get(Donee_id)
    if not Donee:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
        return jsonify({
        "id": Donee.id,
         "nombre": Donee.nombre,
         "email": Donee.email
     }), 200

@jwt_required()
def eliminar_usuario(Donee_id):
    Donee = Donee.query.get(Donee_id)
    if not Donee:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
    db.session.delete(Donee)
    db.session.commit()
    return jsonify({"mensaje": "Usuario eliminado"}), 200 """
