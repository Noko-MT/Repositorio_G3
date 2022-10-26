# Importacion libreria
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from waitress import serve
# Importacion json configuracion
import json

app = Flask(__name__)
cors = CORS(app)

@app.route("/", methods=['GET'])
def initServer():
    json = {}
    json['mensaje'] = 'Server Running.....'
    return jsonify(json)

@app.route("/", methods=["POST"])
def testPOST():
    json = {}
    json['mensaje'] = 'Servidor corriendo POST..'
    return jsonify(json)

def loadConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadConfig()
    print("Service Runing... ("+"http://"+dataConfig['url-backend']+":"+ str(dataConfig['port'])+")")
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])