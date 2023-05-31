from entity import Entity as entity

class Shark(entity):


    def __init__(self):
        super().__init__(2)


    def draw(self):
        return "X"