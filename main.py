import os
from serviço.recebe_dados import RecebeDados

drt = os.path.abspath(r"./")

if __name__ == "__main__":
    print("Começando execução!")
    servidor = RecebeDados(drt)
    servidor.executar()
