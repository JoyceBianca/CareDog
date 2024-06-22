#__init__.py
from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])  # Configuração para ambiente de desenvolvimento

# Importando as rotas após a criação do aplicativo Flask
import routes