from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import config
from src.models import db 
from src.routes.doneesRoutes import doneesBlueprint
from src.routes.donorsRouter import donorsBlueprint
from src.routes.profileRouter import profileBlueprint
from src.routes.contributionsRouter import contributiosBlueprint
from src.routes.addressRouter import addressBlueprint
from src.routes.locationsRouter import locationsBlueprint
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": ["https://unidosporlasangre.integrador.xyz", "http://localhost:4200"]}})

    app.config.from_object(config['development'])
    
    db.init_app(app)
    jwt = JWTManager(app)
    app.register_blueprint(doneesBlueprint, url_prefix="/donees")
    app.register_blueprint(donorsBlueprint, url_prefix="/donors")
    app.register_blueprint(profileBlueprint, url_prefix="/profile")
    app.register_blueprint(contributiosBlueprint, url_prefix="/contributions")
    app.register_blueprint(addressBlueprint, url_prefix="/address")
    app.register_blueprint(locationsBlueprint, url_prefix="/locations")

    return app

# Define app globalmente
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
