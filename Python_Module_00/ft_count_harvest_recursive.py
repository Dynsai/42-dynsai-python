def ft_count_harvest_recursive() -> None:
    until_harvest: int = int(input("Days until harvest: "))

    def print_days(i: int) -> None:
        if i <= until_harvest:
            print(f"Day {i}")
            print_days(i + 1)
        else:
            print("Harvest time!")
    print_days(1)
