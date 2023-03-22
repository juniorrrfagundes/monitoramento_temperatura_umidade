# -*- coding: utf-8 -*-
import json
import os


class Config:

    def __init__(self, drt, arquivo):
        self.dado_config = self.__ler_arquivo(drt, arquivo)

    @staticmethod
    def __ler_arquivo(drt, arquivo):
        arquivo_config = os.path.join(drt, arquivo)
        if os.path.exists(arquivo_config):
            with open(arquivo_config) as arquivo_json:
                dado_json = json.load(arquivo_json)

        return dado_json
