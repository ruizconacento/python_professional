#theory: 

def my_gen():

    """Theoric example"""
    print("Hello World")
    n = 0
    yield n

    print("Hello heaven")
    n = 1
    yield n

    print("Hello hell")
    n = 2
    yield n

a = my_gen()
print(next(a)) #Hello World
print(next(a)) #Hello Heaven
print(next(a)) #Hello Hell
print(next(a)) #StopIteration

#generator expression

my_list = [0,1,4,7,9,10]

my_second_list = [x*2 for x in my_list]

my_second_gen = (x*2 for x in my_list)