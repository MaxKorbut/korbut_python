def say_hello_to_vyacheslav(name: str) -> str:
    """If input_name == Вячеслав: print Привет, Вячеслав else: print Нет такого имени"""
    if name == "Вячеслав":
        return "Привет, Вячеслав"
    else:
        return "Нет такого имени"


if __name__ == "__main__":
    input_name = input("Enter name: ")
    print(say_hello_to_vyacheslav(input_name))
