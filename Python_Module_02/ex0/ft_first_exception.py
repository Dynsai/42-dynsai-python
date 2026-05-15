def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    return temp_int


def test_temperature() -> None:
    temp: int
    for value in ["25", "abc"]:
        print(f"=== Testing '{value}'")
        try:
            temp = input_temperature(value)
            print(f"Temperature is {temp}")
        except ValueError as error:
            print(f"Error: {error}")
        print("Test completed!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("\nAll test completed. End of program")
