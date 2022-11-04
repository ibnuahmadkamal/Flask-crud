from flask import Flask
# from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import config as config

# Initiate flask
app = Flask(__name__)
app.config.from_object('config')

# Initiate service
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# from app.models import postgres
# db.create_all()

@app.route('/', methods=['GET'])
def index():
    return 'hello word'

# register blueprint
from app.api import api_bp
app.register_blueprint(api_bp)
