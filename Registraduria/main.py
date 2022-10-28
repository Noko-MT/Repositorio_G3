from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

import pymongo
import certifi

app = Flask(__name__)
cors = CORS(app)

from Controladores.ControladorPartido import ControladorPartido

miControladorPartido = ControladorPartido()



@app.route("/", methods=['GET'])
def test():
    json = {}
    json['mensaje'] = 'Servidor corriendo...'
    return jsonify(json)

@app.route("/", methods=['POST'])
def testPOST():
    json = {}
    json['mensaje'] = 'Servidor corriendo POST...'
    return jsonify(json)



#Rutas para el controlador PARTIDO

@app.route("/partidos", methods=['GET'])
def indexPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos", methods=['POST'])
def createPartidos():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['PUT'])
def updatePartidos(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['DELETE'])
def deletePartidos(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['GET'])
def showPartidos(id):
    json = miControladorPartido.show(id)
    return jsonify(json)


#############################################

def loadConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    ca = certifi.where()
    client = pymongo.MongoClient(
        "mongodb+srv://admin:admin@cluster0.nvqesnb.mongodb.net/?retryWrites=true&w=majority",
        tlsCAFile=ca)
    db = client.test
    print(db)

    baseDatos = client['bd-registraduria']
    print(baseDatos.list_collection_names())



    dataConfig = loadConfig()
    print("Servicio corriendo.... " + "http://" + dataConfig['url-backend'] + ":" + str(dataConfig['port']))
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])

