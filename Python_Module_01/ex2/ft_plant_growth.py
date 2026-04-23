class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def grow(self) -> None:
        self.height += 0.5

    def get_old(self) -> None:
        self.age += 1

    def info(self) -> None:
        day_word = "day" if self.age == 1 else "days"
        print(f"{self.name}: {self.height}cm, {self.age} {day_word} old")


if __name__ == "__main__":
    def ft_plant_growth() -> None:
        plant1 = Plant("Rose", 25, 12)
        time_to_pass: int = 7
        i: int = 1
        initial_height: float = plant1.height
        print(f"=== Day {i} ===")
        plant1.info()
        while i < time_to_pass:
            print(f"=== Day {i} ===")
            plant1.grow()
            plant1.get_old()
            plant1.info()
            i += 1
        total_grow: float = plant1.height - initial_height
        print(f"Growth this week: {total_grow}cm")
    ft_plant_growth()
