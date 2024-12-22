#!/usr/bin/env python3

import connexion
from openapi_server import encoder
from flask_sqlalchemy import SQLAlchemy
from openapi_server.controllers.vista_controller import import_db_controller
from openapi_server.models.vista import import_db

from flask_cors import CORS

# commit test
app = connexion.App(__name__, specification_dir='./openapi/')
CORS(app.app)
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'Microservicio de Contenidos de una aplicación de tipo Netflix'},
            pythonic_params=True)

app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://api_user:api_password@db_vistas:5432/api_database'
app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 350,        # Tamaño máximo de conexiones en el pool
    'pool_timeout': 30,     # Tiempo máximo de espera para obtener una conexión
    'pool_recycle': 30,   # Tiempo máximo de vida de una conexión (en segundos)
    'max_overflow': 20       # Conexiones extra que pueden crearse si se alcanza el pool_size
}

db = SQLAlchemy(app.app)

import_db_controller(db)
import_db(db)

app.run(port=8082)
