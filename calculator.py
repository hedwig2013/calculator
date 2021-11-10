def addition(a, b):
    return a+b


def substraction(a, b):
    return a-b


def product(a, b):
    return a*b


def division(a, b):
    return a/b


def identity(a, b):
    return b


def main():
    i = input("Die Kettenaufgabe: ")
    operation = '#'
    current_number = ""
    result = 0
    possible_operations = {'+': addition,
                           '-': substraction,
                           '/': division,
                           '*': product,
                           '#': identity}
    for c in i:
        if c.isnumeric and c not in possible_operations:
            current_number += c
        else:
            result, current_number = calculate(
                operation, current_number, possible_operations, result)
            if c in possible_operations:
                operation = c

    final_result,current_number = calculate(operation, current_number,
                             possible_operations, result)

    print(final_result)


def calculate(c, current_number, possible_operations, result):
    if c not in possible_operations:
        return result, current_number
    current_number = float(current_number)
    r = possible_operations[c](result, current_number)
    return r, ""


if (__name__ == "__main__"):
    main()
