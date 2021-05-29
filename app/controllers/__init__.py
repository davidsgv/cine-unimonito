from app import app
from app.controllers.Ciudad import ciudad
from app.controllers.Multiplex import multiplex
from app.controllers.PuntoAgil import puntoAgil


app.register_blueprint(ciudad)
app.register_blueprint(multiplex)
app.register_blueprint(puntoAgil)