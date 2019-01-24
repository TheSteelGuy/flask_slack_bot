import os
class EnvConfig(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.urandom(10)


class DevelopmentEnv(EnvConfig):
    """Configurations for Development."""
    DEBUG = True

class ProductionEnv(EnvConfig):
    """Configurations for Development."""
    DEBUG = True

app_env = {
    'development': DevelopmentEnv,
    'production': ProductionEnv
}


