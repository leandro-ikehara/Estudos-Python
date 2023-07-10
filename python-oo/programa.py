class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # def imprime(self):
    #     print(f'- {self._nome} - {self.ano} - {self._likes}♥')

    def __str__(self) -> str:
        return f'- {self._nome} - {self.ano} - {self._likes}♥'