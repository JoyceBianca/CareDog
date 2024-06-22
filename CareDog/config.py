#config.py
import os

# Configurações do aplicativo Flask
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Caredog123'
    DEBUG = True  # Definir como False em produção
    # Outras configurações...

# Configuração específica para desenvolvimento
class DevelopmentConfig(Config):
    DEBUG = True
    # Configurações adicionais para desenvolvimento

# Configuração específica para produção
class ProductionConfig(Config):
    DEBUG = False
    # Configurações adicionais para produção

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
