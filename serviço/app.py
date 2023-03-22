from flask import Flask, make_response, jsonify, request
from serviço.conexao_banco import ConexaoBanco
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
# cors = CORS(app, resources={r"/sensor": {"origins": "*"}})
CORS(app)
conexao = ConexaoBanco(r"../")


@app.route('/sensor', methods=['GET'])
def pega_info():
    dado = list()
    for item in conexao.ler_banco():
        dado.append(
            {
                'id': item[0],
                'temperatura': item[1],
                'umidade': item[2],
                'data': item[3]
            }
        )
    return make_response(
        jsonify(
            mensagem="Lista do banco",
            Dados=dado
        )
    )


app.run()

# @app.route('/criar', methods=['POST'])
# def criar():
#     item = request.json
#     sensor.append(item)
#     return sensor
