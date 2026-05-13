def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    print(f"Temperature is {temp_int}")
    return temp_int


def test_temperature() -> None:
    for value in ["25", "abc"]:
        print(f"=== Testing '{value}'")

        try:
            input_temperature(value)
        except ValueError as error:
            print(f"Error: {error}")
        print("Test completed!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("\nAll test completed. End of program")
