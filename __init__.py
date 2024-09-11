# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# db = SQLAlchemy()
# migrate = Migrate()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('app.config.Config')

#     db.init_app(app)
#     migrate.init_app(app, db)

#     from .views import book_blueprint
#     app.register_blueprint(book_blueprint)

#     return app




from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Get the configuration name from the environment variable
    config_name = os.getenv('FLASK_CONFIG', 'prd')
    
    # Load configuration from the chosen config class
    from app.config import config_options
    app.config.from_object(config_options[config_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .views import book_blueprint
    app.register_blueprint(book_blueprint)

    return app

