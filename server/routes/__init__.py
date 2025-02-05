from flask import Blueprint

# Initialize the routes blueprint
routes_bp = Blueprint('routes', __name__)

# Import route definitions
from . import example_routes  # Assuming you will create example_routes.py for your routes