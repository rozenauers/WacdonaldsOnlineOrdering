# Written by XJ

# the inventory for a single ingredient

class Inventory(): 
  def __init__(self, name, quantity):
    self._name = name
    self.quantity = quantity # staff access only

  @property
  def name(self):
      return self._name
