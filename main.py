import re


def calcul_factorial(n):
    if n == 0 or n == 1:
        return 1
    rezultat = 1
    for i in range(2, n + 1):
        rezultat *= i
    return rezultat


def calculeaza_sinus(grade):
    pi_aproximat = 3.141592653589793
    x = grade * (pi_aproximat / 180)
    x = x % (2 * pi_aproximat)

    sin_x = 0
    for i in range(10):
        semn = (-1) ** i
        putere_impara = 2 * i + 1
        termen = (x ** putere_impara) / calcul_factorial(putere_impara)
        sin_x += semn * termen

    return round(sin_x, 5)


def converteste(val):
    try:
        return float(val) if '.' in val else int(val)
    except ValueError:
        return val


def evalueaza_expresie_simpla(expr_str):
    """Evaluează o expresie simplă aritmetică (ex: 2*3 sau 13+12) folosind logica ta de CLI v2"""
    tokens = re.findall(r'[a-zA-Z0-9.]+|[+\-*/]', expr_str)
    if not tokens:
        return 0

    rezultat = converteste(tokens[0])
    for i in range(1, len(tokens) - 1, 2):
        op = tokens[i]
        val = converteste(tokens[i + 1])
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
            rezultat /= val if val != 0 else 1
    return rezultat


def main():
    print("--- Calculator CLI v3 (Suport Operații în Sinus) ---")
    while True:
        expr = input("\nExpresie: ").replace(" ", "")

        if expr.lower() == 'iesire':
            break

        # Pasul 1: Căutăm orice apariție de tipul sin(...)
        while True:
            # ReGex-ul prinde tot ce este în paranteza lui sin, inclusiv caractere ca +, -, *, /
            match_sin = re.search(r"sin\((.+?)\)", expr, re.IGNORECASE)
            if not match_sin:
                break

            continut_paranteza = match_sin.group(1)

            # Dacă în paranteză avem o operație (ex: 2*3), o calculăm mai întâi
            if any(op in continut_paranteza for op in ['+', '-', '*', '/']):
                rezultat_interior = evalueaza_expresie_simpla(continut_paranteza)
                grad = float(rezultat_interior)
            else:
                grad = float(continut_paranteza)

            valoare_sin = calculeaza_sinus(grad)
            expr = expr.replace(match_sin.group(0), str(valoare_sin))

        # Pasul 2: Calculul final al întregii expresii rămase
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
                    if val == 0:
                        print("Eroare: Impartire la zero!")
                        eroare = True
                        break
                    rezultat /= val
            except Exception:
                print("Eroare: Operatie invalida.")
                eroare = True
                break

        if not eroare:
            print(f"Rezultat: {rezultat}")


if __name__ == "__main__":
    main()

