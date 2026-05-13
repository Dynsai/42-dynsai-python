def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        integer: int = int("hola")
        print(f"{integer}")
    elif operation_number == 1:
        result1: float = 12 / 0
        print(f"{result1}")
    elif operation_number == 2:
        open("prueba.txt", "r")
    elif operation_number == 3:
        string1: str = "hola"
        number1: int = 3
        result2: int = string1 + number1
        print(f"{result2}")
    else:
        return


def test_error_types() -> None:
    tests: list[int] = [0, 1, 2, 3, 4, 5]
    for test in tests:
        print(f"=== Testing '{test}'")

        try:
            garden_operations(test)
            print("Ejecutado sin errores")
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError
                ) as error:
            print(f"Error: {error}")
    print("All errors types tested successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
