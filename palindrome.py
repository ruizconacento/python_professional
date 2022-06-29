def is_palindrome(string: str) -> bool:
    string = string.replace(" ","").lower() 
    return string == string[::-1]
    #Ana is palindrome

def run():
    print(is_palindrome("ANA"))
    print()

if __name__ == '__main__':
    run()