from flask import Blueprint, jsonify , request

#Model
from app.model.PuntoAgil import PuntoAgil



puntoAgil = Blueprint('puntoAgil', __name__ , url_prefix="/punto-agil/")  

@puntoAgil.route("")
def getPunto():
    #instanciar el modelo
    puntoAgil = PuntoAgil()
    data = data = puntoAgil.buscarPuntoagil(request.json["nombre-usuario"])
    return jsonify({"Multiplex": data,"message":"ok"})


@puntoAgil.route("",methods=["POST"])
def insertPunto():
    puntoAgil = PuntoAgil()
    data = puntoAgil.insertarPuntoagil(request.json["nombre-usuario"], request.json["ubicacion"], request.json["ciudad"])
    return jsonify({"Multiplex": data,"message":"ok"})

@puntoAgil.route("",methods=["PUT"])
def actualizarPunto():
    # instanciar el modelo
    puntoAgil = PuntoAgil()
    
    data = puntoAgil.actualizarPuntoagil(request.json["nombre-usuario"], request.json["ubicacion"], request.json["ciudad"])
    return jsonify({"Multiplex": data,"message":"ok"})

@puntoAgil.route("", methods=["DELETE"])
def borrarPunto():
    # instanciar el modelo
    puntoAgil = PuntoAgil()
    puntoAgil.borrarPuntoagil(request.json["nombre-usuario"])
    return jsonify({"Multiplex": request.json["nombre-usuario"],"message":"ok"})
