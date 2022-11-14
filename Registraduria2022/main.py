#IMPORTACION DE LAS LIBRERIAS QUE SE NECESITAN EN EL PROYECTO
from flask import Flask
from flask import jsonify
from flask import request #PETICIONES GET-POST-PUT-DELETE
from flask_cors import CORS #PERMITIR PETICIONES DESDE CUALQUIER DOMINIO
import json #PERMITE TRABAJAR CON JSON
from waitress import serve #PERMITE CREAR UN SERVIDOR EN MI EQUIPO LOCAL
#LIBRERIAS PARA CONECTAR CON MONGODB
import pymongo
import certifi


app = Flask(__name__)
cors = CORS(app)

#CREAR RUTAS
@app.route("/", methods=['GET'])
def test():
    json = {}
    json['mensaje'] = 'Servidor corriendo...'
    return jsonify(json)

#----Rutas para el controlador PARTIDO
from Controladores.ControladorPartido import ControladorPartido
miControladorPartido = ControladorPartido()#COBSTRUYENDO EL OBJETO

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

#----Rutas para el controlador CANDIDATO
from Controladores.ControladorCandidato import ControladorCandidato
miControladorCandidato = ControladorCandidato()#COBSTRUYENDO EL OBJETO

@app.route("/candidatos", methods=['GET'])
def indexCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidatos", methods=['POST'])
def createCandidatos():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['PUT'])
def updateCandidatos(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['DELETE'])
def deleteCandidatos(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['GET'])
def showCandidatos(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidatos/<string:id_candidato>/partidos/<string:id_partido>", methods=['PUT'])
def setCandidatos(id_candidato, id_partido):
    json = miControladorCandidato.setPartido(id_candidato, id_partido)
    return jsonify(json)


#----Rutas para el controlador MESA
from Controladores.ControladorMesa import ControladorMesa
miControladorMesa = ControladorMesa()#COBSTRUYENDO EL OBJETO

@app.route("/mesas", methods=['GET'])
def indexMesas():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas", methods=['POST'])
def createMesas():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['PUT'])
def updateMesas(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['DELETE'])
def deleteMesas(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['GET'])
def showMesas(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

#----Rutas para el controlador RESULTADO
from Controladores.ControladorResultado import ControladorResultado
miControladorResultado = ControladorResultado()#COBSTRUYENDO EL OBJETO

@app.route("/resultados", methods=['GET'])
def indexResultados():
    json = miControladorResultado.index()
    return jsonify(json)

@app.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['POST'])
def createResultados(id_candidato, id_mesa):
    data = request.get_json()
    json = miControladorResultado.create(data, id_candidato, id_mesa)
    return jsonify(json)

@app.route("/resultados/<string:id_resultado>/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['PUT'])
def updateResultados(id_resultado, id_candidato, id_mesa):
    data = request.get_json()
    json = miControladorResultado.update(id_resultado, data, id_candidato, id_mesa)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['DELETE'])
def deleteResultados(id):
    json = miControladorResultado.delete(id)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['GET'])
def showResultados(id):
    json = miControladorResultado.show(id)
    return jsonify(json)

#################################################################3
#LEER ARCHIVO config.json
def loadConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data
#CREAR EL SERVIDOR
if __name__ == '__main__':
    #CONEXION CON LA BASE DE DATOS MONGO
    ca = certifi.where() #CREACION DEL SERTIFICADO
    dataConfig = loadConfig()
    client = pymongo.MongoClient(dataConfig['data-db-connection'], tlsCAFile = ca)
    db = client.test
    print(db)
    baseDatos = client[dataConfig['name-db']]
    print(baseDatos.list_collection_names())

    # CREAR LA RUTA PARA EJECUTAR EL SERVIDOR
    print("Servicio corriendo.." + "http://" + dataConfig['url-backend'] + ":" + str(dataConfig['port']))
    # MONTAR EL SERVIDOR
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])


