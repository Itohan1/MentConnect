#!/usr/bin/python3
""""""

from models.sign import SignUp
from models import Storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/signs', methods=['GET'], strict_slashes=False)
def get_signs():
    """"""
    all_signs = storage.all(SignUp).values()
    list_signs = []
    for signs in all_signs:
        list_signs.append(signs.to_dict())
    return jsonify(list_users)

@app_views.route('/signs/<sign_id>', methods=['GET'], strict_slashes=False)
def get_user(sign_id):
    """"""
    sign = storage.get(SignUp, sign_id)
    if not sign:
        abort(404)
    return jsonify(sign.to_dict())

@app_views.route('/signs/<sign_id>', methods=['DELETE'], strict_slahes=False)
def delete_signs(sign_id):
    """"""
    sign = storage.get(SignUp, sign_id)

    if not sign:
        abort(404)

    storage.delete(sign)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/signs', methods=['POST'], strict_slashes=False)
def post_signs():
    """"""

    if not reques.get_json():
        abort(400, description="Not a valid Json")

    if 'email' not_in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = SignUp(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/signs/<sign_id>', method=['PUT'], strict_slashes=False)
def put_signs(sign_id):
    """"""
    sign = storage.get(SignUp, sign_id)

    if not sign:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a valid Json")

    ignore = ['id', 'email', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(sign, key, value)
    storage.save()
    return make_response(jsonify(sign.to_dict()), 200)
