# Importacion libreria
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from waitress import serve
# Importacion json configuracion
import json

import pymongo
import certifi

app = Flask(__name__)
cors = CORS(app)

#import controladores
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorResultado import ControladorResultado

#Objeto partidos
miControladorPartido = ControladorPartido()
miControladorCandidato = ControladorCandidato()
miControladorMesa = ControladorMesa()
miControladorResultado = ControladorResultado()

#Mensaje servidor corriendo
@app.route("/", methods=['GET'])
def initServer():
    json = {}
    json['mensaje'] = 'Server Running.....'
    return jsonify(json)

#Rutas Partido
@app.route("/partidos", methods=['GET'])
def indexPartido():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos", methods=['POST'])
def createPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['PUT'])
def updatePartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['DELETE'])
def deletePartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['GET'])
def showPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)

#Rutas Candidato
@app.route("/candidatos", methods=['GET'])
def indexCandidato():
    json = miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidatos", methods=['POST'])
def createCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['PUT'])
def updateCandidato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['DELETE'])
def deleteCandidato(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['GET'])
def showCandidato(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidatos/<string:id_candidato>/partido/<string:id_partido>", methods=['PUT'])
def setCandidato(id_candidato, id_partido):
    json = miControladorCandidato.setPartido(id_candidato, id_partido)
    return jsonify(json)

#Rutas Mesa
@app.route("/mesas", methods=['GET'])
def indexMesa():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas", methods=['POST'])
def createMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['PUT'])
def updateMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['DELETE'])
def deleteMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['GET'])
def showMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

#Rutas Resultados
@app.route("/resultados", methods=['GET'])
def indexResultado():
    json = miControladorResultado.index()
    return jsonify(json)

@app.route("/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=['POST'])
def createResultado(id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.create(data, id_mesa, id_candidato)
    return jsonify(json)

@app.route("/resultados/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=['PUT'])
def updateResultado(id_resultado, id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.update(data, id_resultado, id_mesa, id_candidato)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['DELETE'])
def deleteResultado(id):
    json = miControladorResultado.delete(id)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['GET'])
def showResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)


#Servidor corriendo y importes json
def loadConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadConfig()
    ## Verificar coneccion
    ca = certifi.where()
    client = pymongo.MongoClient(
        dataConfig['data-db-connection'], tlsCAFile=ca)
    db = client.test
    dataBase = client[dataConfig['name-db']]
    print(dataBase.list_collection_names())
    ##
    print("Service Runing... ("+"http://"+dataConfig['url-backend']+":"+ str(dataConfig['port'])+")")
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])