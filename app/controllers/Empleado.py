from flask import Blueprint, json, jsonify , request

#Model
from app.model.Empleado import Empleado



empleado = Blueprint('empleado', __name__ , url_prefix="/empleado/")

@empleado.route("")
def getEmpleado():
    #instanciar el modelo
    empleado = Empleado()
    data = empleado.buscarEmpleado(request.json["codigo"])
    return jsonify({"Empleado": data,"message":"ok"})


@empleado.route("",methods=["POST"])
def insertEmpleado():
    empleado = Empleado()

    #json objects
    codigo = request.json["codigo"]
    tipoDocumento = request.json["tipo-documento"]
    numeroDocumento = request.json["numero-documento"]
    nombres = request.json["nombres"]
    apellido = request.json["apellidos"]
    telefono = request.json["telefono"]
    contrato = request.json["fechaInicioContrato"]
    salario = request.json["salario"]
    estado = request.json["estado"]
    puntoAgil = request.json["punto-agil"]
    multiplex = request.json["multiplex"]

    data = empleado.insertarEmpleado(codigo, tipoDocumento, numeroDocumento, nombres, apellido, 
        telefono, contrato, salario, estado, puntoAgil, multiplex)
    return jsonify({"Empleado": data,"message":"ok"})

@empleado.route("",methods=["PUT"])
def actualizarEmpleado():
    # instanciar el modelo
    empleado = Empleado()

    codigo = request.json["codigo"]
    tipoDocumento = request.json["tipo-documento"]
    numeroDocumento = request.json["numero-documento"]
    nombre = request.json["nombres"]
    apellido = request.json["apellidos"]
    telefono = request.json["telefono"]
    contrato = request.json["fechaInicioContrato"]
    salario = request.json["salario"]
    estado = request.json["estado"]
    PuntoAgil = request.json["punto-agil"]
    multiplex = request.json["multiplex"]
    
    data = empleado.actualizarEmpleado(codigo, tipoDocumento, numeroDocumento, nombre, apellido, 
        telefono, contrato, salario, estado, PuntoAgil, multiplex)
    return jsonify({"Multiplex": data,"message":"ok"})

@empleado.route("", methods=["DELETE"])
def borrarEmpleado():
    # instanciar el modelo
    empleado = Empleado()
    empleado.borrarEmpleado(request.json["codigo"])
    return jsonify({"Empleado": request.json["codigo"],"message":"ok"})
