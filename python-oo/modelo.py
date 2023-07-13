from programa import Programa

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self):
        return f'- {self._nome} - {self.ano} - {self.duracao}min - {self._likes}♥'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'- {self._nome} - {self.ano} - {self.temporadas} temp. - {self._likes}♥'