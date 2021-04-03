from flask import Flask
from flask import Blueprint 

route = Blueprint('route', __name__)


@route.route('/')
def home():
    return "this is a test one "