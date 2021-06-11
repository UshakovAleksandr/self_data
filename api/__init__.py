from flask import Flask, Response
from flask_restful import Api, Resource, abort
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jsonschema_validator import JSONSchemaValidator


app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
ma = Marshmallow(app)
JSONSchemaValidator(app=app, root="api/schemas")
