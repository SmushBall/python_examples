#!/usr/bin/python

# Operations with dict

Laptops = {'DELL':2, 'APPLE':1, 'HP':3, 'LENOVO':4}
Laptops['ACER']= 5
print Laptops

Laptops['LENOVO']=2 # Updating value for the key
print Laptops

print Laptops.get('APPLE',3)
print Laptops.get('ASUS', 6) # checks if ASUS key  value is not present in dict, then return 6

print Laptops.keys()# returns list of keys
print Laptops.values()#returns list of values
print Laptops.items()#returns list of key value pairs
systems = ('mac','linux', 'windows') # List of strings

Creator = {}.fromkeys(systems, 1) #  fromkeys method creates new dict and assigns value 1
print Creator

Creator['mac'] = "Steve Jobs"
Creator['linux'] = "Linus Trovalds"
Creator['windows']='Bill Gates'

print Creator
print Creator.setdefault('Boss', 'Modi')
# Setdefault returns a value if key is present, otherwise inserts the Key value
print Creator

# *************loops
for key in Creator:
	print key

for i in Creator:
    print Creator[i]


#for k, v in Creator.items(): #Something wrong here
#	print ": ".(join(k, v))

# **********Sorting the dict
ikey = Creator.keys()
ikey.sort()

print ikey

for m in ikey:
	print ": ".join((m, str(Creator[m])))

#efficient sorting using built in sorting func
for key in sorted(Creator.iterkeys()): #iterkeys returns an iterator over the dict key val pair
    print "%s: %s " %(key, Creator[key]) 	

# descending sort
for key in sorted(Creator.iterkeys(), reverse=True):
    print "%s: %s " %(key, Creator[key])   

#sorting by value
for key, value in sorted(Creator.iteritems(),
	key = lambda(k,v):(v,k)):
    print "%s : %s" %(key,value)
#the key param takes a func, which indicates how the data is going to be sorted.

#Dictionary view objects vi, vv, vk

vi = Creator.viewitems()
vv = Creator.viewvalues()
vk = Creator.viewkeys()

for m,n in vi:
	print m, n

for n in vv:
	print n

for m in vk:
	print m


print "\n******** Adding two dictionary********\n"

Laptops.update(Creator)#adding two dict
print Laptops

Laptops.pop('windows')# removes a pair with a specified key
print Laptops

del Laptops['DELL']# deles dell pair
print Laptops

Laptops.clear()# clears all
print Laptops
