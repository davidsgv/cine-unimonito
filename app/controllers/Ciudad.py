from flask import Blueprint, jsonify, request

#Model
from app.model.Ciudad import Ciudad


ciudad = Blueprint('ciudad', __name__, url_prefix="/ciudad/")

##listar todas las ciudades
@ciudad.route("list")
def getciudad():
    ciudad = Ciudad()
    data = ciudad.listaCiudades()
    return jsonify({"Ciudades": data,"message":"ok"})

#traer una ciudad especifica
@ciudad.route("")
def insertCiudad():
    ciudad = Ciudad()
    data = ciudad.buscarCiudad(request.json["ciudad"])
    return jsonify({"Ciudad": data,"message":"ok"})

#Crear una ciudad nueva
@ciudad.route("", methods=["POST"])
def nuevaCiudad():
    ciudad = Ciudad()
    data = ciudad.insertCiudad(request.json["ciudad"])
    return jsonify({"Ciudad": data,"message":"ok"})

#Crear una ciudad nueva
@ciudad.route("", methods=["DELETE"])
def borrarCiudad():
    ciudad = Ciudad()
    ciudadPost = request.json["ciudad"]
    ciudad.borrarCiudad(ciudadPost)
    return jsonify({"Ciudad": ciudadPost,"message":"ok"})

#Actualizar una ciudad
@ciudad.route("", methods=["PUT"])
def actualizarCiudad():
    ciudad = Ciudad()

    data = ciudad.actualizarCiudad(request.json["ciudad"],request.json["nuevaCiudad"])
    return jsonify({
        "ciudad": request.json["ciudad"],
        "nuevaCiudad": data,
        "message":"ok"
        })