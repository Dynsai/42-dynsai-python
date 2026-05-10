def ft_count_harvest_iterative() -> None:
    until_harvest: int = int(input("Days until harvest: "))
    for i in range(until_harvest):
        print(f"Day {i+1}")
    print("Harvest time!")
