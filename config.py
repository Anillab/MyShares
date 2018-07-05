import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI='sqlite:////home/benzite/Documents/Projects/Myshares/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY='jihoio@##RQT$WGFSDAGw/.,/>?>?}#@{$^#{%&$*#%#$Fzxcijk}dfg'

class ProdConfig(Config):
    '''
    Pruduction configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
