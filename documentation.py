from abc import ABC, abstractmethod

class Documentation(ABC):  # Interface
    @abstractmethod
    def documentation(self):
        pass

