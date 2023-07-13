from programa import Programa
from modelo import (Filme, Serie)

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    # @property
    # def tamanho(self):
    #     return len(self.__programas)
    def __len__(self):
        return len(self._programas)

vingadores = Filme("Vingadores", 2018, 160)
gog3 = Filme("guardiões da Galáxia vol. 3", 2023, 160)
vingadores.dar_likes()
vingadores.dar_likes()
gog3.dar_likes()
gog3.dar_likes()
vingadores.dar_likes()

the_walking_dead = Serie("Fear The Walking Dead", 2013, 7)
alice_in_borderland = Serie("Alice in Borderland", 2020, 2)
the_walking_dead.dar_likes()
the_walking_dead.dar_likes()
alice_in_borderland.dar_likes()

filmes_e_series = [vingadores, the_walking_dead, alice_in_borderland, gog3]

playlist_maratonar = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_maratonar)}')

for programa in playlist_maratonar:
    print(programa)

