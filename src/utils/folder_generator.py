import os
from utils.time import data_formatada
class folder_generator:
    def __init__(self):
        formatador_padrao = data_formatada()
        data_formatada_padrao = formatador_padrao.pegar_data_formatada()
        self.data_formatada = data_formatada_padrao

    def generate_folder(self,tipo_arquivo):
      nome_pasta = "./data/{}/{}/".format(tipo_arquivo, self.data_formatada)

      if not os.path.exists(nome_pasta):
          os.makedirs(nome_pasta)
          print(f"The directory '{nome_pasta}' was created successfully!")
      else:
          print(f"The directory '{nome_pasta}' already exists.")
