def multiplicity_three(array_list):
    """Print elements that are multiples of 3"""
    new_array = []
    for n in array_list:
        if n % 3 == 0:
            new_array.append(n)
    print(new_array)


if __name__ == "__main__":
    input_array = []
    while True:
        input_value = input("Enter numbers, to exit enter Exit ")
        if input_value != "Exit":
            input_array.append(int(input_value))
        else:
            break
    multiplicity_three(input_array)
