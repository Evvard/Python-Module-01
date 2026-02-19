def garden_operations(charactere) -> str:
    try:
        charactere.isdigit or charactere.isalpha
    except (ValueError):
        try:
            with open('', 'r') as f:
                contenu = f.read()
        except FileNotFoundError:
            return "FileNotFoundError: No such file'{charactere}'"












    else:
        try:
            charactere = int(charactere)
        except (ValueError):
            return "ValueError: invalid literal for int()"
        try:
            charactere = charactere / 0
        except (ZeroDivisionError):
            return "ZeroDivisionError: division by zero"


def test_error_types():
    print("=== Garden Error Types Demo ===", "\n")
    print("Testing ValueError...")
    print("Caught", garden_operations("str"), "\n")
    print("Testing ZeroDivisionError...")
    print("Caught", garden_operations("185"), "\n")

    print("Testing FileNotFoundError...")
    fic = open('mon_fichier.txt', 'r')
    print("Caught", garden_operations(fic), "\n")

    print("Testing KeyError...")

    print("Testing multiple errors together...")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
