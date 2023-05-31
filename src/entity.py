from enum import Enum
import abc





class Entity(abc.ABC):
    pass

    @abc.abstractmethod
    def draw(self):
        pass





class Fish(Entity):

    def __init__(self):
        super().__init__

    def draw(self):
        return ">"





class Shark(Entity):

    def __init__(self):
        super().__init__()

    def draw(self):
        return "X"