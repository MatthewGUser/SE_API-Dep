from app import create_app
from app.models import db
from config import config

app = create_app(config['production'])

with app.app_context():
    db.create_all()