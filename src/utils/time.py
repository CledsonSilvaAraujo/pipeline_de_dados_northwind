from datetime import datetime

class data_formatada:
    def __init__(self, formato="%Y-%m-%d"):
        self.formato = formato

    def pegar_data_formatada(self):
        data_atual = datetime.now()
        return data_atual.strftime(self.formato)



