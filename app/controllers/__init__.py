from app import app
from app.controllers.Ciudad import ciudad


app.register_blueprint(ciudad)