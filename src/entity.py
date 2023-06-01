from enum import Enum
import abc
import math
import random





class Entity(abc.ABC):
    
    last_processed_turn = 0

    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass