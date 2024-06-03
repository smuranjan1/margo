

def main ():
    hello = 0
    hi = 0
    hello = float(input("Give me a number"))
    hi = float(input("Give me another number"))
    print(multiply(hello, hi))

def multiply(one: float, two: float):
    return one*two

if __name__ == "__main__":
    main()