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


def calculate(operation, current_number, possible_operations, result):
    """
    Dies ist der eigentliche Rechner. Es werden 4 Parameter übergeben:
    operation: Die mathematische Operation +, -, *, /
    current_number: Die aktuelle Zahl
    possible_opertions: Ein Dictionary, dass die Operation einer Function zuordnet
    result: Das aktuelle ergebnis, soweit die Kettenrechnung fortgeschritten ist.

    Der Kniff hier ist, dass wir weder if noch switch benutzen, um anhand
    der Operation zu entscheiden, welche Function aufgerufen werden muss.

    In dem Dictionary suchen wir einfach nach der Operation und bekommen so
    die Function zurück, die wir brauchen. Diese können wir direkt aufrufen:
    ```
    possible_operations[operation](result, current_number)
    ```
    Wollte man das mittels if machen, dann sähe das so aus:
    ```
    if operation == '+':
        r=addition(result,current_number)
    else if operation == '-':
        r=subtraction(result,current_number)
    else if operation == '*':
        r=product(result,current_number)
    else if operation == '/':
        r=division(result,current_number)
    ```

    Wie Du siehst, wird das Dictionary mit der Zurodnung der Operanden
    zu den benötigten Funktionen dieser Funktion übergeben. Warum ich
    das mache? Um Dir zu zeigen, dass man Funktionen wie Daten und Variablen zwischen
    anderen Funktionen herumreichen kann.
    """
    if operation not in possible_operations:
        return result, current_number
        
    current_number = float(current_number)
    r = possible_operations[operation](result, current_number)
    return r, ""

# Wenn dieser Code nicht als Modul aufgreufen wird, dann rufe main auf.
# Ansonsten passiert nichts.
if (__name__ == "__main__"):
    main()
