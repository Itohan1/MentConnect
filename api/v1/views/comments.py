#!/usr/bin/python3
""""""

from models.Comments import Comments
from models.sign import SignUp
from models.Blog import Blog
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/blogs/<blog_id>/comments', methods=['GET'], strict_slashes=False)
def get_comments(blog_id):
    """"""

    list_comments = []
    blog = storage.get(Blog, blog_id)
    if not blog:
        abort(404)
    for comment in blog.comments:
        list_comments.append(comment.to_dict())
    return jsonify(list_comments)

@app_views.route('/comments/<comment_id>', methods=['DELETE'], strict_slashes=False)
def delete_comments(comment_id):
    """"""

    comment = storage.get(Comments, comment_id)
    if not comment:
        abort(404)
    storage.delete(comment)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/blogs/<blog_id>/comments', methods=['POST'], strict_slashes=False)
def post_comments(blog_id):
    """"""

    blog = storage.get(Blog, blog_id)
    if not blog:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a valid json")

    if 'sign_id' not in request.get_json():
        abort(400, description="Please first signUp")

    data = request.get_json()
    user = storage.get(SignUp, data['sign_id'])
    
    if not user:
        abort(404)

    if 'comments' not in request.get_json():
        abort(400, description="Please add a comment")

    data['blog_id'] = blog_id
    instance = Comments(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/comments/<comment_id>', methods=['PUT'], strict_slashes=False)
def put_comments(comment_id):
    """"""

    comment = storage.get(Comments, comment_id)

    if not comment:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a valid Json")

    ignore = ['id', 'sign_id', 'blog_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(comment, key, value)
    storage.save()

    return make_response(jsonify(comment.to_dict()), 200)
