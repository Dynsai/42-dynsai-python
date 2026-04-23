class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = 0
        self._age: int = 0

        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height: int) -> None:
        if new_height >= 0:
            self._height = new_height
        else:
            print("Error: La altura introducida no puede ser negativa")
    
    def set_age(self, new_age: int) -> None:
        if new_age > 0:
            self._age = new_age
        else:
            print("Error: La edad introducida no puede ser negativa")

    def get_name(self) -> str:
        return self._name
    
    def get_height(self)  -> float:
        return self._height
    
    def get_age(self) -> int:
        return self._age
    
    def info(self) -> None:
        name = self.get_name()
        height = self.get_height()
        age = self.get_age()
        day_word = "day" if age == 1 else "days"
        print(f"{name}: {height}cm, {age} {day_word} old")


if __name__ == "__main__":
    def ft_plant_factory() -> None:
        plant = Plant("Rose", 15, 10)
        plant.info()
        plant.set_height(-20)
        plant.set_age(1)
        plant.info()
    ft_plant_factory()
