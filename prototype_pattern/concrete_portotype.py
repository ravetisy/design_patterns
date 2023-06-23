from prototype_1 import Prototype
from copy import deepcopy


class ConcretePrototype(Prototype):
    def clone(self):
        return deepcopy(self)
