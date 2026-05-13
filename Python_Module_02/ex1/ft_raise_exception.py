def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    if temp_int < 0:
        print(f"Temperature is {temp_int}")
        raise ValueError(
            "Temperature is not in range! "
            "Temperature is too cold!"
        )
    elif temp_int > 40:
        print(f"Temperature is {temp_int}")
        raise ValueError(
            "Temperature is not in range! "
            "Temperature is too hot!"
        )
    print(f"Temperature is {temp_int}. It's in range!")
    return temp_int


def test_temperature() -> None:
    tests: list[str] = ["25", "abc", "100", "-50"]
    for test in tests:
        print(f"=== Testing '{test}'")

        try:
            input_temperature(test)
        except ValueError as error:
            print(f"Error: {error}")
        print("~ Test completed!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
    print("\nAll test completed. End of program")
