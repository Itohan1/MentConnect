#!/usr/bin/python3
""""""

from models.Blog import Blog
from models.sign import SignUp
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/signs/<sign_id>/blogs', methods=['GET'], strict_slashes=False)
def get_blogs(sign_id):
    """"""
    list_blogs = []
    sign = storage.get(SignUp, sign_id)
    if not sign:
        abort(404)
    for blog in sign.blog:
        list_blogs.append(blog.to_dict())
    return jsonify(list_blogs)

@app_views.route('/blogs/<blog_id>', methods=['DELETE'], strict_slashes=False)
def delete_blog(blog_id):
    """"""
    blog = storage.get(Blog, blog_id)
    if not blog:
        abort(404);
    storage.delete(blog)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/signs/<sign_id>/blogs', methods=['POST'], strict_slashes=False)
def post_blog(sign_id):
    """"""
    sign = storage.get(SignUp, sign_id)
    if not sign:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a json")

    if 'blog' not in request.get_json():
        abort(400, description="Please select type a blogpost")

    data = request.get_json()
    instance = Blog(**data)
    instance.sign_id = sign.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/blogs/<blog_id>', methods=['PUT'], strict_slashes=False)
def put_blog(blog_id):
    """"""
    blog = storage.get(Blog, blog_id)
    if not blog:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a Json")

    ignore = ["id", "sign_id", "created_at", "updated_at"]

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(blog, key, value)
    storage.save()
    return make_response(jsonify(blog.to_dict()), 201)
