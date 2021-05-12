from flask import Blueprint, jsonify

#Model
from app.model.Ciudad import Ciudad


ciudad = Blueprint('ciudad', __name__)

@ciudad.route("/ciudad")
def getciudad():
    #instanciar el modelo
    ciudad = Ciudad()
    # controler = Controller()

    data = ciudad.buscarCiudad("Bogotá")
    return jsonify({"Ciudad": data,"message":"ok"})


@ciudad.route("/ciudad/<string:ciudad_nombre>")
def insertCiudad(ciudad_nombre):
    # instanciar el modelo
    ciudad = Ciudad()

    data = ciudad.insertCiudad(ciudad_nombre)
    return jsonify({"Ciudad": data,"message":"ok"})


# @app.route("/products", methods=["POST"])
# def addProduct():
#     print(request.json)
#     new_product = {
#         "name": request.json["name"],
#         "price": request.json["price"],
#         "quantity": request.json["quantity"]
#     }
#     products.append(new_product)
#     return jsonify({"message": "Product added successfully", "products": products})