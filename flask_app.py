from app import create_app
from app.models import db
from config import config

app = create_app(config['production'])

# Update Swagger config
app.config.update({
    'SWAGGER': {
        'title': 'Your API',
        'uiversion': 3,
        'specs_route': '/swagger/',
        'host': 'se-api-dep.onrender.com',  # Remove https:// prefix
        'schemes': ['https']
    }
})

with app.app_context():
    db.create_all()