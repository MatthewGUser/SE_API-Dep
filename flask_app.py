from app import create_app
from app.db import db
from app.config import config

app = create_app(config['production'])

app.config.update({
    'SWAGGER': {
        'title': 'Your API',
        'uiversion': 3,
        'specs_route': '/swagger/',
        'host': 'se-api-dep.onrender.com',
        'schemes': ['https']
    }
})

with app.app_context():
    db.create_all()