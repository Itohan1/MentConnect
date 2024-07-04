#!/usr/bin/python3
""""""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.chosenpath import *
from api.v1.views.role import *
from api.v1.views.specialization import *
from api.v1.views.requests import *
from api.v1.views.signs import *
