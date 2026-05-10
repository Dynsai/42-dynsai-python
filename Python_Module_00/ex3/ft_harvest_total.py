def ft_harvest_total() -> None:
    harvest1: int = int(input("Day 1 harvest: "))
    harvest2: int = int(input("Day 2 harvest: "))
    harvest3: int = int(input("Day 3 harvest: "))
    harvest_total: int = harvest1 + harvest2 + harvest3
    print(f"Total harvest: {harvest_total}")
