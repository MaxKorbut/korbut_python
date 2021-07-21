def say_hello(value):
    """If input value > 7: print Привет"""
    if value > 7:
        print("Привет")


if __name__ == "__main__":
    input_value = int(input("Enter number: "))
    say_hello(input_value)
