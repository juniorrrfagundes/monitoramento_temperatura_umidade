from serviço.config import Config
import mysql.connector


class ConexaoBanco:

    def __init__(self, drt):
        config = Config(drt, "config.json")
        self.config_banco = config.dado_config['config_banco']
        self.conexao = self.__conectar_banco(self.config_banco)
        self.cursor = self.__cursor(self.conexao)

    @staticmethod
    def __conectar_banco(config):

        try:
            conexao = mysql.connector.connect(**config)
            return conexao
        except mysql.connector.Error as err:
            print(err)

    @staticmethod
    def __cursor(conexao):
        return conexao.cursor()

    # Tratar tabelas com ORM
    def inserir_no_banco(self, temperatura, umidade, data):
        try:
            sql = f"INSERT INTO sensor_dht22 (temperatura, umidade, data) VALUES ({temperatura}, {umidade}, '{data}');"
            self.cursor.execute(sql)
            self.conexao.commit()
        except Exception as err:
            print(err)

    def ler_banco(self):
        self.cursor.execute("SELECT * FROM sensor_dht22")
        dados = self.cursor.fetchall()
        return dados
