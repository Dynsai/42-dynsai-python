class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def info(self) -> None:
        day_word = "day" if self.age == 1 else "days"
        print(f"{self.name}: {self.height}cm, {self.age} {day_word} old")

plant_list = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
]

plants: list[Plant] = []

if __name__ == "__main__":
    def ft_plant_factory() -> None:
        print("=== Plant Factory Output ===")
        for list_data in plant_list:
            plant: Plant = Plant(list_data[0], list_data[1], list_data[2])
            plants.append(plant)
            plant.info()
    ft_plant_factory()
