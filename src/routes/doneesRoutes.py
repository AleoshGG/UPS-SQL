from flask import Blueprint, request
from src.controllers.doneesController import createDonee, updateDonee, login, getDonee, delete, getDoneeById, add_photo, get_photo, getPhotoByName

doneesBlueprint = Blueprint('donees', __name__)

@doneesBlueprint.route('/add', methods=['POST'])
def addDonee():
    data = request.get_json()
    return createDonee(data)

@doneesBlueprint.route('/update', methods=['PUT'])
def putDonee():
    data = request.get_json()
    return updateDonee(data)

@doneesBlueprint.route('/login', methods=['POST'])
def loginR():
    data = request.get_json()
    return login(data)

@doneesBlueprint.route('/profile', methods=['GET'])
def viewProfile():
    return getDonee()

@doneesBlueprint.route('/search/<int:id_donee>', methods=['GET'])
def search(id_donee):
    return getDoneeById(id_donee)

@doneesBlueprint.route('/deleteAccount', methods=['DELETE'])
def deleteAccount():
    return delete()

@doneesBlueprint.route('/addPhoto', methods=['POST'])
def addPhoto():
    data = request.files.get('photo')
    return add_photo(data)

@doneesBlueprint.route('/photo', methods=['GET'])
def viewPhoto():
    return get_photo()

@doneesBlueprint.route('/photo/<string:name>', methods=['GET'])
def viewPhotoName(name):
    return getPhotoByName(name)