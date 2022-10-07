from Node import Node

from abc import ABCMeta, abstractmethod
class Problem(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, initial, goal):

        if not isinstance(initial, Node):
            raise TypeError('node type is required for initial')
        if not isinstance(goal, Node):
            raise TypeError('node type is required for initial')

        self.initial = initial
        self.goal = goal

    @abstractmethod
    def expand(self, node):

        raise NotImplementedError
