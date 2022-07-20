#Un iterador es la manera de recorrer una ciclo internamente

my_list = [1,2,3,4,5,6]
my_iter = iter(my_list)
#NEXT devuelve el primer valor del iterador que estemos recorriendo
#print(next(my_iter)) -> out: 1
#while try
print("I command mi iter and i make my list: " + str(my_list))
#estructura interna de un ciclo FOR
print("While starts")
while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break
print("While ends and For starts: ")
#FOR es una estructura de datos que recorre todos los iteradores hasta encontrar un error 
for element in my_list:
    print(element)

#Construir un iterador (Protocolo de los iteradores con double under score iter)
#__x__ es necesario para crear una clase

print("Last line of code")