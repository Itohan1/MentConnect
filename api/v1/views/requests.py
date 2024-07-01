#!/usr/bin/python3
""""""

from models.Requests import Requests 
from models.sign import SignUp
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/roles/<role_id>/requests', methods=['GET'], strict_slashes=False)
def get_requests(role_id):
    """"""
    
    role = storage.get(Role, role_id)
    if not role:
        abort(404)

    requests = [request.to_dict() for request in role.requests]
    return jsonify(requests)

@app_views.route('/requests/<request_id>', methods=['GET'], strict_slashes=False)
def get_request(request_id):
    """"""
    request = storage.get(Requests, request_id)
    if not request:
        abort(404)
    return jsonify(request.to_dict())

@app_views.route('requests/<request_id>', methods['DELETE'], strict_slashes=False)
def delete_request(request_id):
    """"""
    request = storage.get(Requests, request_id)
    if not request:
        abort (404)
    storage.delete(request)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/roles/<role_id>/requests', methods=['POST'], strict_slashes="False")
def post_request(role_id):
    """"""
    role = storage.get(Roles, role_id)
    if not role:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a json")

    if 'sign_id' not in request.get_json:
        abort(400, description="Please SignUp")


    data = request.get_json()
    sign = storage.get(SignUp, data['sign_id'])

    if not sign:
        abort(404)

    if 'request' not in request.get_json():
        abort(400, description="Missing request")

    data["role_id"] = role_id
    instance = Request(**data)
    instance.save
    return make_response(jsonify(instance.to_dict()), 201)

    
@app_views.route('/requests/request_id', method=['PUT'], strict_slahes=False)
def put_request(request_id):
    """"""
    request = storage.get(Request, request_id)
    if not request:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, description="Not a Json")

    ignore = ["id", "sign_id", "created_at", "updated_at"]

    for key, value in data.items():
        if key not in ignore:
            setattr(request, key, value)
    storage.save()
    return make_resonse(jsonify(request.to_dict()), 200)
