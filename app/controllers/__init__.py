from app import app
from app.controllers.Ciudad import ciudad
from app.controllers.Multiplex import multiplex


app.register_blueprint(ciudad)
app.register_blueprint(multiplex)