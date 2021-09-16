import os

from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
            SECRET_KEY='TH1S_K3Y-for_fl4sksession',
            DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
            DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
            DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
            DATABASE=os.environ.get('FLASK_DATABASE'),
            DATABASE_PORT=os.environ.get('FLASK_DATABASE_PORT')
            )
    from . import db 
    db.init_app(app)
    
    from . import auth
    app.register.blueprint(auth.b)

    @app.route('/hola')
    def hola():
            return 'hola flask app'

    return app