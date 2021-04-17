class Player_4:

    def __init__(self, name, cards, vcards, coins):
        self.__name = name
        self.__cards = cards
        self.__vcards = vcards
        self.__coins = coins

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, value):
        self.__cards = value

    @property
    def vcards(self):
        return self.__vcards

    @vcards.setter
    def vcards(self, value):
        self.__vcards = value      

    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self, value):
        self.__coins = value  
