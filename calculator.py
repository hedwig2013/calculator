def addition(a, b) -> float:
    """
    Diese Funktion addiert die Zahlen a und b. 
    """
    return a+b


def substraction(a, b) -> float:
    """
    Diese Funktion subtrahiert Zahl b von a. 
    """
    return a-b


def product(a, b) -> float:
    """
    Diese Funktion multipliziert die Zahlen a und b. 
    """
    return a*b


def division(a, b) -> float:
    """
    Diese Funktion teilt die Zahl a durch b. 
    """
    return a/b


def identity(a, b) -> float:
    """
    Diese Funktion gibt einfach b zurück und ignoriert a.
    """
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
        if c.isnumeric():
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
