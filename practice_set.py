# [1, 1, 1, 2, 3, 4] -> [1, 2, 3, 4]

def remove_duplicates(lista):
    without_duplicates = []
    for element in lista:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))

if __name__=='__main__':
    run()

#challenge: Make this example with sets
"""


my code here



"""