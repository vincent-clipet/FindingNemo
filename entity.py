from enums import EntityTypes as EntityTypes

class Entity():


    type = None


    def __init__(self, type: EntityTypes):
        if type == 1:
            self.type = type
            
            
    def draw(self):
        return "."
