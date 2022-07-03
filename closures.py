def make_divisor(n):
    def divisor(x):
        return x/n
    return divisor

def run():
    num = make_divisor(3)
    print(num(456))

if __name__ == "__main__":
    run()