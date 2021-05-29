from flask import Blueprint, jsonify , request

#Model
from app.model.Multiplex import Multiplex



multiplex = Blueprint('multiplex', __name__ , url_prefix="/multiplex/")  

@multiplex.route("")
def getmultiplex():
    #instanciar el modelo
    multiplex = Multiplex()

    data = multiplex.buscarMultiplex(request.json["multiplex"])
    return jsonify({"Multiplex": data,"message":"ok"})


@multiplex.route("",methods=["POST"])
def insertMultiplex():
    multiplex = Multiplex()

    data = multiplex.insertMultiplex(request.json["nombre"], request.json["direccion"], request.json["localidad"], request.json["ciudad"])
    return jsonify({"Multiplex": data,"message":"ok"})

@multiplex.route("",methods=["PUT"])
def actualizarMultiplex():
    # instanciar el modelo
    multiplex = Multiplex()

    #nuevo multiplex
    nuevoMultiplex = request.json["nuevo_multiplex"]

    multiplexNombre = request.json["multiplex_nombre"]
    nombre = nuevoMultiplex["nombre"]
    direccion = nuevoMultiplex["direccion"]
    localidad = nuevoMultiplex["localidad"]
    ciudad = nuevoMultiplex["ciudad"]

    data = multiplex.actualizarMultiplex(multiplexNombre, nombre, direccion, localidad, ciudad)
    return jsonify({"Multiplex": data,"message":"ok"})

@multiplex.route("", methods=["DELETE"])
def borrarmultiplex():
    # instanciar el modelo
    multiplex = Multiplex()

    multiplex_nombre = request.json["multiplex"]

    multiplex.borrarMultiplex(multiplex_nombre)
    return jsonify({"Multiplex": multiplex_nombre,"message":"ok"})
