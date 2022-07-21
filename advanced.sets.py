#Example

#operation with sets

my_set = {1,2,3,4,4,5}
my_set1 = {1,2,5,6}

#| union
my_set3 = my_set | my_set1
print(my_set3)

# & intersection
my_set4 = my_set & my_set1
print(my_set4)

# - difference for each side m - n or n - m
my_set5 = my_set - my_set1
print(my_set5)

#^symmetric_difference
my_set6 = my_set  my_set1
print(my_set6)
