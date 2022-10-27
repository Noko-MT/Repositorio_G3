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

#import Controladores


#Mensaje servidor corriendo
@app.route("/", methods=['GET'])
def test():
    json = {}
    json['mensaje'] = 'Servidor corriendo...'
    return jsonify(json)

#Rutas app


#Conexion con mongo
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