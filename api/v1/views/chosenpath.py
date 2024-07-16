#!/usr/bin/python3
""""""

from models.Chosen_path import ChosenPath
from models.sign import SignUp
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/signs/<sign_id>/chosenpaths', methods=['GET'], strict_slashes=False)
def get_chosenpaths(sign_id):
    """"""
    list_chosenpaths = []
    sign = storage.get(SignUp, sign_id)
    if not sign:
        abort(404)
    for chosenpath in sign.chosenpaths:
        list_chosenpaths.append(chosenpath.to_dict())
    return jsonify(list_chosenpaths)

@app_views.route('/chosenpaths/<chosenpath_id>', methods=['GET'], strict_slashes=False)
def get_chosenpath(chosenpath_id):
    """"""
    chosenpath = storage.get(ChosenPath, chosenpath_id)
    if not chosenpath:
        abort(404)
    return jsonify(chosenpath.to_dict())

@app_views.route('/chosenpaths/<chosenpath_id>', methods=['DELETE'], strict_slashes=False)
def delete_chosenpath(chosenpath_id):
    """"""
    chosenpath = storage.get(ChosenPath, chosenpath_id)
    if not chosenpath:
        abort(404);
    storage.delete(chosenpath)
    storage.save()

@app_views.route('/signs/<sign_id>/chosenpaths', methods=['POST'], strict_slashes=False)
def post_chosenpath(sign_id):
    """"""
    sign = storage.get(SignUp, sign_id)
    if not sign:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a json")

    if 'career_name' not in request.get_json():
        abort(400, description="Please choosepath")

    data = request.get_json()
    instance = ChosenPath(**data)
    instance.sign_id = sign.id
    instance.save()
    chosen_id = str(instance.sign_id)
    response = make_response(jsonify(instance.to_dict()), 201)
    response.set_cookie('chosen_id', chosen_id, secure=True, path='/')
    return response

@app_views.route('/chosencookie', methods=['GET'], strict_slashes=False)
def chosen_path():
    logging.debug("Entering protected_resource endpoint")
    chosen_id = request.cookies.get('chosen_id')
    logging.debug(f"Retrieved chosen_id from cookies: {chosen_id}")
    if not chosen_id:
        return jsonify({"error": "Chosen ID cookie not found"}), 400

    chosen = storage.get(ChosenPath, chosen_id)
    if not chosen:
        return jsonify({"error": "Invalid Chosen ID"}), 404

    return jsonify(chosen.to_dict())

@app_views.route('/chosenpaths/<chosenpath_id>', methods=['PUT'], strict_slashes=False)
def put_chosenpath(chosenpath_id):
    """"""
    chosenpath = storage.get(ChosenPath, chosenpath_id)
    if not chosenpath:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a Json")

    ignore = ["id", "sign_id", "created_at", "updated_at"]

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(chosenpath, key, value)
    storage.save()
    return make_response(jsonify(chosenpath.to_dict()), 201)
