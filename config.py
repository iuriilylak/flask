import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    """Base configuration."""
    secret_key = 'my_precious'
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS=False


