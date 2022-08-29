from abc import ABC, abstractmethod

class Parser(ABC):

    def __init__(self):
        ...

    @classmethod
    @abstractmethod
    def parse(self):
        raise NotImplementedError()
