import random
from .entity import Entity


class Shark(Entity):

    MAX_ENERGY = -1
    ENERGY_GAIN = -1
    BASE_ENERGY = -1
    BIRTH_INTERVAL = -1
    
    energy = -1
    last_birth = 0
    last_update = 0


    def __init__(self, energy_gain, base_energy, birth_interval, max_energy):
        
        self.ENERGY_GAIN = energy_gain
        self.BASE_ENERGY = base_energy
        self.BIRTH_INTERVAL = birth_interval
        self.MAX_ENERGY = max_energy

        self.energy = base_energy
        
        super().__init__()

    
    def draw(self):
        return "X"
    

    def refill_energy(self):
        self.energy = min(self.MAX_ENERGY, self.energy + self.ENERGY_GAIN)
    

    

    def update(self, grid, current_cell):

        # this entity was already updated during current turn => skip
        if self.last_update == grid.turn:
            return
        else:
            self.last_update = grid.turn
            self.energy -= 1

        # No energy left, shark is dead :(
        if self.energy < 0:
            current_cell.clear()
            return

        free_cells = grid.get_surrounding_free_cells(current_cell.x, current_cell.y)
        fish_cells = grid.get_surrounding_fishs(current_cell.x, current_cell.y)
        
        can_move = len(fish_cells) + len(free_cells) > 0
        can_eat = len(fish_cells) > 0
        can_birth = self.last_update > self.last_birth + self.BIRTH_INTERVAL and (can_move or can_eat)
        
        newborn = None
        destination = None


        # Pre-calculate everything
        if can_birth:
            newborn = self.pre_birth(grid, current_cell)
            self.last_birth = grid.turn
        if can_eat:
            destination = self.pre_eat(grid, current_cell, fish_cells)
            self.refill_energy()
        if can_move and destination is None:
            destination = self.pre_move(grid, current_cell, free_cells)
        
        # Apply all calculations
        if can_birth:
            destination.set_entity(self)
            current_cell.set_entity(newborn)
        elif can_eat:
            destination.set_entity(self)
            current_cell.clear()
        elif can_move:
            destination.set_entity(self)
            current_cell.clear()
        else: # can't do anything
            pass
    



    def pre_move(self, grid, current_cell, free_cells):
        destination = random.choice(free_cells)
        return destination
    
    def pre_eat(self, grid, current_cell, fish_cells):
        destination = random.choice(fish_cells)
        destination.clear()
        return destination

    def pre_birth(self, grid, current_cell):
        newborn = Shark(self.ENERGY_GAIN, self.BASE_ENERGY, self.BIRTH_INTERVAL, self.MAX_ENERGY)
        newborn.last_update = grid.turn
        newborn.last_birth = grid.turn
        return newborn