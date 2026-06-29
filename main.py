import re


def calcul_factorial(n):
    """Calculează n! (factorial)"""
    if n == 0 or n == 1:
        return 1
    rezultat = 1
    for i in range(2, n + 1):
        rezultat *= i
    return rezultat


def calculeaza_sinus(grade):
    """Calculează sin(x) folosind aproximarea Seriei Taylor"""
    # 1. Convertim gradele în radiani (Pi aproximativ format simplu)
    pi_aproximat = 3.141592653589793
    x = grade * (pi_aproximat / 180)

    # 2. Reducem unghiul în intervalul [-2*PI, 2*PI] pentru a evita erorile la numere uriașe
    x = x % (2 * pi_aproximat)

    sin_x = 0
    # Calculăm primii 10 termeni ai seriei (suficient pentru precizie maximă)
    for i in range(10):
        # Semnul alternează: + - + -
        semn = (-1) ** i
        # Puterile și factorialele sunt doar numere impare: 1, 3, 5, 7...
        putere_impara = 2 * i + 1

        termen = (x ** putere_impara) / calcul_factorial(putere_impara)
        sin_x += semn * termen

    return round(sin_x, 5)  # Rotunjim la 5 zecimale pentru un output curat


def converteste(val):
    try:
        return float(val) if '.' in val else int(val)
    except ValueError:
        return val


def main():
    print("--- Calculator CLI v2 ---")
    while True:
        # Scoatem toate spatiile libere pentru a evita erorile la scriere
        expr = input("\nExpresie: ").replace(" ", "")

        if expr.lower() == 'iesire':
            break

        match_sin = re.match(r"^sin\((.+?)\)$", expr, re.IGNORECASE)
        if match_sin:
            try:
                grad = float(match_sin.group(1))
                print(f"Rezultat: {calculeaza_sinus(grad)}")
            except ValueError:
                print("Eroare: Introdu un număr valid în interiorul sin(). Ex: sin(45)")
            continue

        tokens = re.findall(r'[a-zA-Z0-9.]+|[+\-*/]', expr)
        if not tokens:
            continue

        rezultat = converteste(tokens[0])
        eroare = False

        for i in range(1, len(tokens) - 1, 2):
            op = tokens[i]
            val = converteste(tokens[i + 1])

            try:
                if op == '+':
                    try:
                        rezultat += val
                    except TypeError:
                        rezultat = str(rezultat) + str(val)
                elif op == '-':
                    rezultat -= val
                elif op == '*':
                    rezultat *= val
                elif op == '/':
                    rezultat /= val
            except Exception:
                print("Eroare: Operatie invalida (ex: scadere intre litere).")
                eroare = True
                break

        if not eroare:
            print(f"Rezultat: {rezultat}")


if __name__ == "__main__":
    main()