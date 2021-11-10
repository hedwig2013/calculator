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

    Es gibt andere Mittel, aber ich möchte den Ball flach halten.

    Wenn Du Dir auch die vorhergehenden Funktionen ansiehst, dann stellst Du fest,
    dass alle die gleichen Parameter haben. Das ist für die Funktion `calculate`
    sehr wichtig. Denn die wird von den Funktionen, die ihr übergeben werden, einfach
    erwarten, dass sie alle zwei Parameter entgegen nehmen.
    """
    return b


def main():
    """
    Wenn dieser Code nicht als Modul aufgerufen wird, dann wird auch dieses Main aufgerufen.
    """
    # Zunächst lassen wir uns eine Kettenaufgabe stellen.
    # Kettenaufgabe, weil wir Punkt-Vor-Strich und weitere Wertigkeiten
    # der mathematischen Operatoren mal einfach ignorieren. Wir werden
    # einfach von links nach rechts die Operatoren mit einer Zahl
    # auf das bisherige Ergebnis anwenden.
    the_input = input("Die Kettenaufgabe: ")

    # Die Raute oder auch Umgangssprachlich Lattenzaun
    # habe ich einfach so als Platzhalter genommen.
    # Amanfang wird es keine `current_number geben` und auch kein
    # `result` geben. Somit muss calculate wissen, dass die erste
    # Zahl einfach nur der Anfang ist und noch nicht mit einem
    # mathematischen Operator verarbeitet werden soll.
    operation = '#'
    current_number = ""
    result = 0

    # Dieses Dictionary ist ein Trick. Eine Funktion kann wie ein
    # Wert einer Variablen herumgereicht werden. Deshalb ordne ich in
    # diesem Dictionary jedem Operator eine Funktion zu. Das Dictionary
    # speicher ich in der Variablen possible_operations.
    possible_operations = {
                            '+': addition,
                            '-': substraction,
                            '/': division,
                            '*': product,
                            '#': identity
                        }
    # Jedes Zeichen in der eingegebenen Zeichenkette wird nun
    # durchlaufen.
    for character in the_input:
        # Ist das Zeichen eine Ziffer,
        if character.isnumeric() or character=='.':
            # dann fügen wir das Zeichen der Zeichenkette `current_number` hinzu.
            current_number += character
        # Wenn das Zeichen keine Ziffer ist,
        else:
            # dann könnte es sein, dass das aktuelle Zeichen ein Operator ist.
            # Lassen wir also einen Versuch mit `calculate` laufen.
            # Sollte `calculate` damit nichts anfangen können, dann kommen hier
            # die Werte unverändert zurück. Andernfalls kommt für
            # `current_number` eine leere Zeichenkette zurück. Damit ist
            # wieder Platz für eine neue Zahl.
            result, current_number = calculate(
                operation, current_number, possible_operations, result)
            # Jeder gelesene Operator wird hier für den nächsten Durchlauf gespeichert.
            # Der Grund ist, dass jeder Operator erst angewendet darf, wenn die nachfolgende Zahl
            # gelesen wurde. Beispiele für 11+22-3
            # Ist 11+ gelesen, dann ist eben die Frage, was soll addiert werden. Also muss
            # erst weitergelesen werden, um die 22 zu erfassen. Der Trick mit dem '#' hat defür
            # gesorgt, dass in `result` die 11 steht. Wenn die 22 aber gelesen ist, dann ist der
            # nächste Operator ein '-'. Daher müssen wir uns hier immer merken, welches der
            # zuletzt gelesen Operator war. Denn dann können wir calculate völlig richtig
            # die 11 das '+' und die gerade gelsene 22 übergeben.
            # Mittels dem for laufen wir aber von links nach rechts, Zeichen für Zeichen und müssen
            # nie zurück gehen.
            if character in possible_operations:
                operation = character

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

    # Wenn die operation nicht in dem übergebenen Dictionary enthalten ist,
    # dann werden die bestehenden Zahlen unverändert einfach zurück gegeben.
    if operation not in possible_operations:
        return result, current_number

    # Wurde die Operation im Dictionary gefunden, dann kommen wir hier an.
    # Da die Funktion main mit Zeichenketten und einzelnen Zeichen arbeitet,
    # müssen wir erst aus der Zeichenkette eine echte Zahl mache, hier eine
    # Fließkommazahl.
    current_number = float(current_number)
    # Mit dem zuvor beschriebenen Trick, holen wir nun aus dem Dictionary, mit Hilfe
    # der Operation als Index, die Funktion heraus. Und rufen Sie direkt auf.
    # Alternativ hätten wir schreiben können:
    # f = possible_operations[operation]
    # r = f(result, current_number)
    r = possible_operations[operation](result, current_number)
    # Damit main erkennt, dass die Operation durchgeführt wurde,
    # Geben wir nun das neue Ergebnis r und eine leere Zeichenkette zurück.
    return r, ""

# Wenn dieser Code nicht als Modul aufgreufen wird, dann rufe main auf.
# Ansonsten passiert nichts.
if (__name__ == "__main__"):
    main()
