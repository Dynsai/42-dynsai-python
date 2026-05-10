#! python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        day_word = "day" if self.age == 1 else "days"
        print(f"{self.name}: {self.height}cm, {self.age} {day_word} old")


if __name__ == "__main__":
    def ft_garden_data() -> None:
        print("=== Garden Plant Registry ===")
        plant1 = Plant("Rose", 25, 12)
        plant2 = Plant("Sunflower", 80, 45)
        plant3 = Plant("Cactus", 15, 120)

        plant1.show()
        plant2.show()
        plant3.show()
    ft_garden_data()
