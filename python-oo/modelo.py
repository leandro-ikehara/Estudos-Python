from programa import Programa


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # def imprime(self):
    #     print(f'- {self._nome} - {self.ano} - {self.duracao}min - {self._likes}♥')

    def __str__(self):
        return f'- {self._nome} - {self.ano} - {self.duracao}min - {self._likes}♥'


vingadores = Filme("Vingadores", 2018, 160)
gog3 = Filme("guardiões da Galáxia vol. 3", 2023, 160)
vingadores.dar_likes()
vingadores.dar_likes()
gog3.dar_likes()
gog3.dar_likes()
vingadores.dar_likes()


# print(f'- Filme: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - ♥{vingadores._likes}')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # def imprime(self):
    #     print(f'- {self._nome} - {self.ano} - {self.temporadas} temp. - {self._likes}♥')

    def __str__(self):
        return f'- {self._nome} - {self.ano} - {self.temporadas} temp. - {self._likes}♥'


# class Playlist(list):
#     def __init__(self, nome, programas) -> None:
#         self.nome = nome
# self.programas = programas
# super().__init__(programas)

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.__programas = programas

    @property
    def listagem(self):
        return self.__programas

    @property
    def tamanho(self):
        return len(self.__programas)

    # def tamanho(self):
    #     return len(self.programas)


the_walking_dead = Serie("Fear The Walking Dead", 2013, 7)
alice_in_borderland = Serie("Alice in Borderland", 2020, 2)
the_walking_dead.dar_likes()
the_walking_dead.dar_likes()
alice_in_borderland.dar_likes()
# print(f'- Série: {the_walking_dead.nome} - Ano: {the_walking_dead.ano} - Temporadas: {the_walking_dead.temporadas} - ♥{the_walking_dead._likes}')

filmes_e_series = [vingadores, the_walking_dead, alice_in_borderland, gog3]

# for programa in filmes_e_series:
#     programa.imprime()
playlist_maratonar = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_maratonar.listagem)}')

for programa in playlist_maratonar.listagem:
    print(programa)