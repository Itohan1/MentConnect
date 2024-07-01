#!/usr/bin/python3
""""""

from models.Role import Role
from models.sign import SignUp
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/signs/<sign_id>/roles', methods=['GET'], strict_slashes=False)
def get_roles(sign_id):
    """"""
    list_roles = []
    sign = storage.get(SignUp, sign_id)
    if not sign:
        abort(404)
    for role in sign.roles:
        list_roles.append(role.to_dict())
    return jsonify(list_roles)

@app_views.route('/signs/<sign_id>/roles', methods=['POST'], strict_slashes="False")
def post_role(sign_id):
    """"""
    sign = storage.get(SignUp, sign_id)
    if not sign:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a json")

    if role not in request.get_json:
        abort(400, description="Please choose select role")

    data = request.get_json()
    instance = Role(**data)
    instance.sign_id = sign.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

