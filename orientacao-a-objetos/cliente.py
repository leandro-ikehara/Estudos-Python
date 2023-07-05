class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property #equivalente ao getter
    def nome(self):
        return self.__nome.title()

    @nome.setter #equivalente ao setter
    def nome(self, nome):
        self.__nome = nome