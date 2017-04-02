from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec

app = Flask(__name__)
app.config['SECRET_KEY'] = 'verysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# initialization
api = Api(app)

# extensions
db = SQLAlchemy(app)


app.config.update({
    'APISPEC_SPEC': APISpec(
        title='API',
        version='v1',
        plugins=['apispec.ext.marshmallow'],
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',
})
docs = FlaskApiSpec(app)


from app import main
