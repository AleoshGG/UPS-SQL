from flask import Blueprint, request
from src.controllers.donorsController import createDonor, login_usuario
from flask_jwt_extended import JWTManager

donorsBlueprint = Blueprint('donors', __name__)

@donorsBlueprint.route('/add', methods=['POST'])
def addDonor():
    data = request.get_json()
    return createDonor(data)

# @donorsBlueprint.route('/update/<int:id_donee>', methods=['PUT'])
# def putDonee(id_donee):
#     data = request.get_json()
#     return (id_donee, data)

# @usuario_blueprint.route('/users_base', methods=['POST'])
# def crear_usuario_base_ruta():
#     data = request.get_json()
#     return crear_usuario_base(data)

@donorsBlueprint.route('/login', methods=['POST'])
def login_ruta():
    data = request.get_json()
    return login_usuario(data)

# @usuario_blueprint.route('/profile', methods=['GET'])
# def obtener_usuario_ruta():
#     return obtener_usuario()

# @usuario_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
# def eliminar_usuario_ruta(user_id):
#     return eliminar_usuario(user_id)
