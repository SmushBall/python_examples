#!/usr/bin/python
# SmushBall Oct 4, 2015
# Dictionary datatype in python has key value pairs.
# It is represented by {}.
# It is mutable and can contain mixed data types.
# It is unordered collection of key value pairs.
# Unique elements can be present in dictionary

#Below are few ways to create a dictionary


Days= {"sun": "sunday", "mon":"monday"}
Numbers = dict(one=1, two=2) # Using the dict function
Players = {} # creating an empty dictionary
Players["Cricket"] = "Sachin" # Assigning the values for the keys
Players["Football"]="Messi"
Players["Tennis"]= "Roger"
Players["Golf"]="Tiger Woods"
Players["Poker"]="Dan Bilzerian"

d = {i:object() for i in range(4)} #creating a dict, where key will be 0,1,2,3
print Days
print Numbers
print Players
print d