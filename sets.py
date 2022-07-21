#theory

#how the Set is
my_set = {1,2,3,4,} #main example set
print("my set = ", my_set)

my_set2 = {1,1,2,2,3,3, True, False, False}
print("my set = ", my_set2) #if you get your variables into a set, the function print retusn unique

"""my_set3 = {[1,2,3],1} 
print("my set is = ", my_set3) #List is a mutable structure so can´t be in set"""

#declare empty set
empty_set = {}
print(type(empty_set)) #output -> "class dict"

empty_set = set()
print(type(empty_set)) #out -> "Class set"

#casting
my_list = [1,1,1,3,3,4,5]
my_set4 = set(my_list)
print(my_set4)

my_tuple = ("hola", "hola", "hola", 1)
my_set5 = set(my_tuple)
print(my_set5)

#modify a set

my_set6 = {1,2,3,"hola", True}
print(my_set6)

my_set6.add(4) #for one element
print(my_set6)

my_set6.update([1,2,3,4,5,6]) #for more than one element
print(my_set6)

my_set6.update((8,9,7),{10,11,21}) #for differents structures
print(my_set6)

my_set6.discard("hola") #Discard is for any element, in the set and not
print(my_set6)

my_set6.remove(10)
print(my_set6)

my_set6.pop()
print(my_set6)

my_set6.remove(10)
print(my_set6)