from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import config
from src.routes.doneesRoutes import doneesBlueprint
from src.routes.donorsRouter import donorsBlueprint
from src.models.donee import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])
    db.init_app(app)
    jwt = JWTManager(app)
    app.register_blueprint(doneesBlueprint, url_prefix="/donees")
    app.register_blueprint(donorsBlueprint, url_prefix="/donors")
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
