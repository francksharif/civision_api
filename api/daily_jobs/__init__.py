from flask import Blueprint 

jobs = Blueprint('jobs', __name__, url_prefix='/api/v1/jobs')

from . import routes