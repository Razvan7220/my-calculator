import re


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