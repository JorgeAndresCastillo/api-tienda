from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

"""
#ruta de prueba de servidor
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message":"pong"})
"""

# ruta para obtener toda el diccionario de productos con metodo get
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products":products, "mesage":"product's List"})


#ruta para obtener un atributo de la lista que esta dentro del diccionario por metodo get
@app.route('/products/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    # dentro un arreglo vamos a almacenar la lista de producto que va a busar el usuario recoriendo products por medio de un for y se condicciona si el producto en el valor de 'name' == al que se esta buscando 
    productsFound = [ products for products in products if products['name'] == product_name ]
    # se verifica que si este el producto si existe si la longitud de la lista es mayor a 0 es que existe
    if( len(productsFound) > 0):
        return jsonify({"product" : productsFound[0]})

    return jsonify({"message": "product not found"})

#ruta para agregar productos con POST
@app.route('/products', methods=['POST'])
def addProduct():
    #se almacena en un lista json lo que llega por post
    productsNew = {
        "name":request.json['name'],
        "price":request.json['price'],
        "quantity": request.json['quantity']
    }

    products.append(productsNew)

    name = request.json['name']

    productsFound = [ products for products in products if products['name'] == name ]
    # se verifica que si este el producto si existe si la longitud de la lista es mayor a 0 es que existe
    if( len(productsFound) > 0):
        return jsonify({"message":"product added succesfulluy", "product agg":productsFound[0] })

    return jsonify({
        "message": "product no found in add"
    })

@app.route('/products/<string:product_name>', methods=['PUT'])
def productEdit(product_name):
    productFound = [products for products in products if products['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']

        return jsonify({
            "message" : "products update",
            "product" : productFound[0]
        })

    return jsonify({
        "message": "product no found in edit"
    })

@app.route('/products/<string:product_name>', methods=['DELETE'])
def productDelete(product_name):
    productFound = [ products for products in products if products['name'] == product_name]

    if ( len(productFound) > 0 ):
        products.remove(productFound[0])

        return jsonify({
            "message":"product delete list"
        })



    return jsonify({
        "message": "product no found in delete"
    })

