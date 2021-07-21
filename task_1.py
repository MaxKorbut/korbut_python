def say_hello(value: int) -> str:
    """If input value > 7: print Привет"""
    if value > 7:
        return "Привет"


if __name__ == "__main__":
    input_value = int(input("Enter number: "))
    func_return = say_hello(input_value)
    if func_return:
        print(func_return)
