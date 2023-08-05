#!/usr/bin/env python3

import os
import connexion

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from openapi_server import encoder

import db.models


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.app.config['JSON_AS_ASCII'] = False
    app.add_api('openapi.yaml',
                arguments={'title': 'Swagger Kattakke - OpenAPI 3.0'},
                pythonic_params=True)
    # SQLALCHEMY_DATABASE_URI = "sqlite://:memory"
    
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
        'user': 'kattakke',
        'password': 'kattakke',
        'host': os.getenv('POSTGRESQL_HOST', '127.0.0.1'),
        'name': 'kattakke'
    }))
    db.models.init_db(SQLALCHEMY_DATABASE_URI)

    app.run(port=8080)


if __name__ == '__main__':
    main()
