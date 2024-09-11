import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.urandom(32)  
   
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

    @staticmethod
    def init_app(app):
        """Initialize the application with specific configurations."""
        pass

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db' 

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://library:123@localhost:5432/library_db'  
    UPLOADED_PHOTOS_DEST = 'app/static/uploads' 


config_options = {
    'dev': DevelopmentConfig,
    'prd': ProductionConfig
}
