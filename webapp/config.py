class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@127.0.0.1:3306/test_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True