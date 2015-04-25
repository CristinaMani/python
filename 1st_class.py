#!/usr/bin/env python
 
# a trivial class with:
# - two attributes (myName, myColour)
# - one shared attribute (dogCount)
# - one method (bark)
class Dog:
	dogCount = 0	# this is a shared attribute
 
	def __init__(self, name, colour):	# this is a contructor
		self.myname = name		# create an attribute "myname"
		self.mycolour = colour		# create an attribute "mycolour"
		Dog.dogCount += 1		# increment shared attr value
 
	def bark(self):
		print '%s is barking: Bark!' % self.myname
 
# note that "self" above is a reference to the object on which given method is
# executed, you don't have to pass this manually
 
dog1 = Dog("dasher", "black")	# creates a new instance of the class
dog2 = Dog("hannibal", "yellow")  # creates a new instance of th class
 
# let's access the attributes
print 'dog1 name is %s' % dog1.myname
print 'dog1 colour is %s' % dog1.mycolour
print 'dog2 name is %s' % dog2.myname
print 'dog2 colour is %s' % dog2.mycolour
 
# and call some methods
dog1.bark()
dog2.bark()
 
# and access the shared attribute 
print 'There are this many dogs: %d' % Dog.dogCount
 