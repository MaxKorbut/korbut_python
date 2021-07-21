def say_hello_to_vyacheslav(name):
    """If input_name == Вячеслав: print Привет, Вячеслав else: print Нет такого имени"""
    if name == "Вячеслав":
        print("Привет, Вячеслав")
    else:
        print("Нет такого имени")


if __name__ == "__main__":
    input_name = input("Enter name: ")
    say_hello_to_vyacheslav(input_name)
