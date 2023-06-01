import random
from .entity import Entity


class Fish(Entity):

    BIRTH_INTERVAL = -1
    DEATH_AGE = -1

    age = 0
    last_birth = 0
    last_update = 0


    def __init__(self, birth_interval, death_age):
        self.BIRTH_INTERVAL = birth_interval
        self.DEATH_AGE = death_age
        # super().__init__

    def draw(self):
        return "."
    

    def update(self, grid, current_cell):

        # this entity was already updated during current turn => skip
        if self.last_update == grid.turn:
            return
        else:
            self.last_update = grid.turn
            self.age += 1

        # Nemo dies of old age, RIP
        if self.age > 40:
            current_cell.clear()
            return

        free_cells = grid.get_surrounding_free_cells(current_cell.x, current_cell.y)
        
        # if it's possible to move
        if len(free_cells) > 0:

            # Fish has not given birth in more than 'birth_interval' turns
            if self.last_update > self.last_birth + self.BIRTH_INTERVAL:
                # Update parent
                self.last_birth = grid.turn
                destination = random.choice(free_cells)
                destination.set_entity(self)
                # Create & update child
                newborn = Fish(self.BIRTH_INTERVAL, self.DEATH_AGE)
                newborn.last_update = grid.turn
                newborn.last_birth = grid.turn
                current_cell.set_entity(newborn)
            else:
                destination = random.choice(free_cells)
                destination.set_entity(self)
                current_cell.clear()
            
        # no available adjacent cell
        else: # TODO
            pass
