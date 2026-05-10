class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = 0
        self._age: int = 0

        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height: float) -> None:
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

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self) -> None:
        self.set_height(self.get_height() + 15)

    def get_old(self) -> None:
        self.set_age(self.get_age() + 10)

    def extra_info(self) -> None:
        pass

    def info(self) -> None:
        name = self.get_name()
        height = self.get_height()
        age = self.get_age()
        day_word = "day" if age == 1 else "days"
        print(f"{name}: {height}cm, {age} {day_word} old")
        self.extra_info()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, bloom: bool) -> None:
        super().__init__(name, height, age)
        self._color: str = "Blanco"
        self._bloom: bool = False

        self.set_color(color)
        self.set_bloom(bloom)

    def set_color(self, new_color: str) -> None:
        self._color = new_color

    def set_bloom(self, blooming: bool) -> None:
        self._bloom = blooming

    def get_color(self) -> str:
        return self._color

    def get_bloom(self) -> bool:
        return self._bloom

    def extra_info(self) -> None:
        color = self.get_color()
        bloom = self.get_bloom()
        name: str = self.get_name()
        print(f"Color: {color}")
        if not bloom:
            print("Not blooming yet")
            self.set_bloom(True)
            print(f"##[Asking the {name} to bloom]")
            self.info()
        if bloom:
            print("Blooming!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: int, shade: bool) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: int = 1
        self._shade: bool = False

        self.set_trunk_diameter(trunk_diameter)
        self.set_shade(shade)

    def set_trunk_diameter(self, new_trunk_diameter: int) -> None:
        self._trunk_diameter = new_trunk_diameter

    def set_shade(self, giving_shade: bool) -> None:
        if giving_shade is not self._shade:
            self._shade = not self._shade

    def get_trunk_diameter(self) -> int:
        return self._trunk_diameter

    def get_shade(self) -> bool:
        return self._shade

    def extra_info(self) -> None:
        trunk_diameter = self.get_trunk_diameter()
        height: float = self.get_height()
        shade = self.get_shade()
        name: str = self.get_name()
        shade_area: float = height * trunk_diameter
        print(f"Trunk diameter: {trunk_diameter}cm")
        if not shade:
            print(f"##[Asking the {name} to produce shade]")
            self.set_shade(True)
            print(
                    f"Tree now produces a shade of {shade_area / 10000}"
                    f" square m ({height}cm * {trunk_diameter}cm)"
                )
        if shade:
            print(
                    f"Tree now produces a shade of {shade_area / 10000}"
                    f" square m ({height}cm * {trunk_diameter}cm)"
                )


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season: str = "October"
        self._nutritional_value: int = 20

        self.set_harvest_season(harvest_season)
        self.set_nutritional_value(nutritional_value)

    def set_harvest_season(self, new_harvest_season: str) -> None:
        self._harvest_season = new_harvest_season

    def set_nutritional_value(self, new_nutritional_value: int) -> None:
        self._nutritional_value = new_nutritional_value

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    def grow_vegetable(self) -> None:
        super().grow()
        super().get_old()
        self._nutritional_value += 15

    def extra_info(self) -> None:
        harvest_season = self.get_harvest_season()
        nutritional_value: int = self.get_nutritional_value()
        name: str = self.get_name()
        height: float = self.get_height()
        age: int = self.get_age()
        print(f"Harvest season: {harvest_season}")
        print(f"Nutritional value: {nutritional_value}kcal")
        print(f"##[Make the {name} grow for 10 days]")
        self.grow_vegetable()
        height = self.get_height()
        age = self.get_age()
        nutritional_value = self.get_nutritional_value()
        print(f"{name}: {height}cm, {age} days old")
        print(f"Harvest season: {harvest_season}")
        print(f"Nutritional value: {nutritional_value}kcal")


if __name__ == "__main__":
    def ft_plant_types() -> None:
        print("=== Garden Plant Types ===")
        print("=== Flower")
        plant = Flower("Rose", 15, 10, "Red", False)
        plant.set_height(20)
        plant.set_age(1)
        plant.set_color("red")
        plant.set_bloom(False)
        plant.info()

        print("=== Tree")
        plant2 = Tree("Pine", 15, 10, 10, False)
        plant2.set_height(200)
        plant2.set_age(15)
        plant2.set_trunk_diameter(45)
        plant2.set_shade(False)
        plant2.info()

        print("=== Vegetable")
        plant3 = Vegetable("Tomatoe", 15, 10, "april", 0)
        plant3.set_height(15)
        plant3.set_age(1)
        plant3.set_harvest_season("october")
        plant3.set_nutritional_value(0)
        plant3.info()
    ft_plant_types()
