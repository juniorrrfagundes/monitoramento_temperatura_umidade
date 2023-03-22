from paho.mqtt import client as mqtt_client
from serviço.config import Config
from serviço.conexao_banco import ConexaoBanco


class RecebeDados:
    def __init__(self, drt):
        config = Config(drt, "config.json")
        self.config_servidor = config.dado_config['config_servidor']
        self.conexao_banco = ConexaoBanco(drt)

    def conecta_servidor(self) -> mqtt_client:
        # BRUXARIA ISSO AQUI
        servidor = str(self.config_servidor['servidor'])

        def conexao(client, userdata, flags, rc):
            if rc == 0:
                print("Conectado ao servidor!")
            else:
                print("Falha ao conectar. codigo: %d\n", rc)

        client = mqtt_client.Client(self.config_servidor['cliente'])
        client.on_connect = conexao
        client.connect(servidor)
        return client

    def recebe_mensagem(self, client: mqtt_client):

        def inserir_dados(client, userdata, msg):
            print(f"Mensagem `{msg.payload.decode()}` de `{msg.topic}`")
            dado = "110,110,1999-03-03"
            dado = dado.split(",")
            self.conexao_banco.inserir_no_banco(float(dado[0]), float(dado[1]), dado[2])

        client.subscribe(self.config_servidor['topico'])
        client.on_message = inserir_dados

    def executar(self):
        cliente = self.conecta_servidor()
        self.recebe_mensagem(cliente)
        cliente.loop_forever()
