#!/usr/bin/env python

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print self.name
        print self.age
        
sloth = Animal("Pixie", 1)
ocelot = Animal("Tooth_Fairy", 3)    
hippo = Animal("George", 27)
print hippo.health
print sloth.health
print ocelot.health
print hippo.description()