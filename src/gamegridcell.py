from .entity import Entity
from .fish import Fish
from .shark import Shark


class GameGridCell():

    x = -1
    y = -1
    entity = None


    def __init__(self, x, y, entity):
        self.x = x
        self.y = y
        self.entity = entity


    def draw(self):
        if self.entity is None:
            return " "
        elif isinstance(self.entity, Entity):
            return self.entity.draw()
        

    def set_entity(self, entity):
        self.entity = entity


    def clear(self):
        ret = self.entity
        self.entity = None
        return ret
    

    def is_empty(self):
        return self.entity is None
    def is_fish(self):
        return isinstance(self.entity, Fish)
    def is_shark(self):
        return isinstance(self.entity, Shark)