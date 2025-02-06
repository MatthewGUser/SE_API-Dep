from app import create_app
from app.models import db
from app.config import config

app = create_app(config['production'])

app.config.update({
    'SWAGGER': {
        'title': 'Your API',
        'uiversion': 3,
        'specs_route': '/swagger/',
        'host': 'your-app-name.onrender.com',
        'schemes': ['https']
    }
})

with app.app_context():
    db.create_all()