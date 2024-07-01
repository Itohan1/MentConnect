#!/usr/bin/python3
""""""

from models.Specialization import Specialization
from models.sign import SignUp
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/signs/<sign_id>/specializations', methods=['GET'], strict_slashes=False)
def get_specializations(sign_id):
    """"""
    list_specializations = []
    sign = storage.get(SignUp, sign_id)
    if not sign:
        abort(404)
    for specialization in sign.specializations:
        list_specializations.append(specialization.to_dict())
    return jsonify(list_specializations)

@app_views.route('/specializations/<specialization_id>', methods=['DELETE'], strict_slashes=False)
def delete_specialization(specialization_id):
    """"""
    specialization = storage.get(Specialization, specialization_id)
    if not specialization:
        abort(404);
    storage.delete(specialization)
    storage.save()

@app_views.route('/signs/<sign_id>/specializations', methods=['POST'], strict_slashes="False")
def post_specialization(sign_id):
    """"""
    sign = storage.get(SignUp, sign_id)
    if not sign:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a json")

    if specialization not in request.get_json:
        abort(400, description="Please select specialization")

    data = request.get_json()
    instance = Specialization(**data)
    instance.sign_id = sign.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/specializations/specialization_id', method=['PUT'], strict_slahes=False)
def put_specialization(specialization_id):
    """"""
    specialization = storage.get(Specialization, specialization_id)
    if not specialization:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a Json")

    ignore = ["id", "sign_id", "created_at", "updated_at"]

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(specialization, key, value)
    storage.save()
    return make_resonse(jsonify(specialization.to_dict()), 201)
