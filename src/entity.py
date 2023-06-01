from enum import Enum
import abc
import random





class Entity(abc.ABC):
    
    last_processed_turn = 0

    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def update_empty_turn(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass





class Fish(Entity):

    age = 0 # TODO: unused
    last_birth = 0
    last_update = 0
    BIRTH_INTERVAL = 0

    def __init__(self, birth_interval):
        self.BIRTH_INTERVAL = birth_interval
        # super().__init__

    def draw(self):
        return "."

    def update_empty_turn(self):
        last_processed_turn += 1
        age += 1
    

    def update(self, grid, current_cell, surroundings):

        # this entity was already updated during current turn => skip
        if self.last_update == grid.turn:
            return
        else:
            self.last_update = grid.turn
            self.age += 1

        # get a list of currently available cells
        free_cells = []
        for i in range(0, len(surroundings)):
            adjacent_cell = surroundings[i]
            if adjacent_cell.is_empty():
                free_cells.append(adjacent_cell)
        
        # if it's possible to move
        if len(free_cells) > 0:

            # Fish has not given birth in more than 'birth_interval' turns
            if self.last_update > self.last_birth + 5:
                # Update parent
                self.last_birth = grid.turn
                destination = random.choice(free_cells)
                destination.set_entity(self)
                # Create & update child
                newborn = Fish(self.BIRTH_INTERVAL)
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

        
    





class Shark(Entity):

    MAX_ENERGY = -1
    ENERGY_GAIN = -1
    energy = -1
    last_update = 0

    def __init__(self, max_energy, energy_gain):
        self.MAX_ENERGY = max_energy
        self.energy = max_energy
        self.ENERGY_GAIN = energy_gain
        super().__init__()

    def draw(self):
        return "X"
    
    def update_empty_turn(self):
        last_processed_turn += 1
        health -= 1
    
    def update(self):
        pass