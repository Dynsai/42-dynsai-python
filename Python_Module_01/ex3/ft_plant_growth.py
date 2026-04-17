class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        self.height += 0.5

    def age(self) -> None:
        self.age += 1

    def info(self) -> None:
        day_word = "day" if self.age == 1 else "days"
        print(f"{self.name}: {self.height}cm, {self.age} {day_word} old")        


plant1 = Plant("Rose", 25, 12)

time_to_pass: int = 7
i: int = 0
initial_height: int = plant1.height
while i < time_to_pass:
    print(f"=== Day {i} ===")
    plant1.grow()
    plant1.age()
    plant1.info()
    i += 1
total_grow: int = plant1.height - initial_height
print(f"Grow this week: {total_grow}cm")
