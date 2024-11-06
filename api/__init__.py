from flask import Flask 
from config import Config
from .daily_jobs import jobs
from extensions import swagger


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    swagger.init_app(app)

    # Register Blueprints
    app.register_blueprint(jobs)
    
    return app