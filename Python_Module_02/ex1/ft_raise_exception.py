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
    for value in ["25", "abc", "100", "-50"]:
        print(f"=== Testing '{value}'")

        try:
            input_temperature(value)
        except ValueError as error:
            print(f"Error: {error}")
        print("~ Test completed!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
    print("\nAll test completed. End of program")