from app import api, db, docs
from flask import redirect, request

from flask_apispec import use_kwargs, marshal_with, doc
from flask_apispec.views import MethodResource

from marshmallow import fields, Schema


class TemplateModel(db.Model):
    __tablename__ = 'template'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(64), index=True)


@doc(tags=['Template'])
class Template(MethodResource):
    def get(self):
        """ Template route

        """
        pass


api.add_resource(Template, '/api/template')

docs.register(Template)
