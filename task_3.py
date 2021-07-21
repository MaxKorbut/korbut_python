def multiplicity_three(array_list: list) -> list:
    """Print elements that are multiples of 3"""
    new_array = []
    for n in array_list:
        if n % 3 == 0:
            new_array.append(n)
    return new_array


if __name__ == "__main__":
    input_array = []
    while True:
        input_value = input("Enter numbers, to exit enter Exit: ")
        if input_value.isdigit():
            input_array.append(int(input_value))
        else:
            if input_value == "Exit":
                break
            else:
                print(f"{input_value} is not a number, try again")
                continue
    print(multiplicity_three(input_array))
