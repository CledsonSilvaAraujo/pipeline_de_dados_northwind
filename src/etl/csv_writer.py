import csv
from utils.time import data_formatada
class csv_writer:
    def __init__(self, nome_arquivo, cabecalho=None):
        self.nome_arquivo = nome_arquivo
        self.cabecalho = cabecalho
        self.dados = []

    def adicionar_linha(self, linha):
        self.dados.append(linha)

    def escrever_csv(self):
        try:
            formatador_padrao = data_formatada()
            with open("./data/csv/{}/{}".format(formatador_padrao.pegar_data_formatada(),self.nome_arquivo), mode="w", newline="") as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                if self.cabecalho:
                    escritor_csv.writerow(self.cabecalho)
                escritor_csv.writerows(self.dados)
            print(f"Arquivo {self.nome_arquivo} criado com sucesso!")
        except Exception as e:
            print("Ocorreu uma exceção:", e)



