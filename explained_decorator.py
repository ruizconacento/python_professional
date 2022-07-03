def decorator(func):
    def wrapper():
        print("I´m add code to function")
        func()
    return wrapper

def run():
    @decorator
    def greeting():
        print("Hola!")

    @decorator
    def greeting2():
        print("Upper")
    #Azúcar sintáctica greeting = decorator(greeting)
    greeting()
    greeting2()

if __name__ == "__main__":
    run()