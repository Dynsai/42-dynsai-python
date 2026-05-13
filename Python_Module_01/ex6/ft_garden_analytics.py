class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float
        self._age: int
        self._statistics: Plant.Statistics = Plant.Statistics()

        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
        else:
            print("Height can't be negative!")

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
        else:
            print("Age can't be negative!")

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self) -> None:
        self.set_height(self.get_height() + 15)
        self._statistics.set_grow_calls()

    def get_old(self) -> None:
        self.set_age(self.get_age() + 10)
        self._statistics.set_age_calls()

    def get_statistics(self) -> "Plant.Statistics":
        return self._statistics

    def extra_show(self) -> None:
        pass

    @staticmethod
    def check_age(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        return cls("Unknow", 0.0, 0)

    def show(self) -> None:
        self._statistics.set_show_calls()
        name = self.get_name()
        height = self.get_height()
        age = self.get_age()
        day_word = "day" if age == 1 else "days"
        print(f"{name}: {height}cm, {age} {day_word} old")
        print(f"+ Is {age} days older than a year? {Plant.check_age(age)}\n")
        self.extra_show()

    class Statistics:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def set_grow_calls(self) -> None:
            self._grow_calls += 1

        def set_age_calls(self) -> None:
            self._age_calls += 1

        def set_show_calls(self) -> None:
            self._show_calls += 1

        def get_grow_calls(self) -> int:
            return self._grow_calls

        def get_age_calls(self) -> int:
            return self._age_calls

        def get_show_calls(self) -> int:
            return self._show_calls

        def display(self) -> None:
            print("=== Calls")
            print(f"{self.get_grow_calls()} grow calls.")
            print(f"{self.get_age_calls()} age calls.")
            print(f"{self.get_show_calls()} show calls\n")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, bloom: bool) -> None:
        super().__init__(name, height, age)
        self._color: str = "Blanco"
        self._bloom: bool = False
        self._seeds: Flower.Seed = Flower.Seed()

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

    def extra_show(self) -> None:
        color = self.get_color()
        bloom = self.get_bloom()
        name: str = self.get_name()
        seeds_number: int = self._seeds.get_seeds()
        print(f"Color: {color}")
        if not bloom:
            print("Not blooming yet")
            print(f"##[Asking the {name} to bloom]")
            self.set_bloom(True)
        if bloom:
            print("Blooming!")
            self._seeds.set_seeds(True)
            seeds_number = self._seeds.get_seeds()
        print(f"Seeds: {seeds_number}")

    class Seed:
        def __init__(self) -> None:
            self._seeds: int = 0

        def set_seeds(self, bloom: bool) -> None:
            if bloom:
                self._seeds = 42

        def get_seeds(self) -> int:
            return self._seeds


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float, shade: bool) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = 1
        self._shade: bool = False
        self._statistics: Tree.Statistics = Tree.Statistics()

        self.set_trunk_diameter(trunk_diameter)
        self.set_shade(shade)

    def set_trunk_diameter(self, new_trunk_diameter: float) -> None:
        self._trunk_diameter = new_trunk_diameter

    def set_shade(self, giving_shade: bool) -> None:
        self._shade = giving_shade

    def produce_shade(self) -> None:
        shade: bool = self.get_shade()
        self._statistics.produce_shade_calls += 1
        if not shade:
            self.set_shade(True)
        else:
            print("Tree already produces shade")

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def get_shade(self) -> bool:
        return self._shade

    def extra_show(self) -> None:
        trunk_diameter: float = self.get_trunk_diameter()
        height: float = self.get_height()
        shade: bool = self.get_shade()
        name: str = self.get_name()
        shade_area: float = height * trunk_diameter
        print(f"Trunk diameter: {trunk_diameter}cm")
        if not shade:
            print(f"{name} doesn't produces a shade")
        if shade:
            print(f"{name} now produces a shade of {shade_area / 10000}")
            print("square meters")

    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self.produce_shade_calls: int = 0

        def get_produce_shade_calls(self) -> int:
            return self.produce_shade_calls

        def display(self) -> None:
            print("=== Calls")
            print(f"{self.get_grow_calls()} grow calls.")
            print(f"{self.get_age_calls()} age calls.")
            print(f"{self.get_show_calls()} show calls")
            print(f"{self.get_produce_shade_calls()} shade calls\n")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season: str = "October"
        self._nutritional_value: int = 20
        self._statistics: Vegetable.Statistics = Vegetable.Statistics()

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
        print(f"##[Make the {self.get_name()} grow for 10 days]")
        super().grow()
        super().get_old()
        self._nutritional_value += 15

    def get_statistics(self) -> "Plant.Statistics":
        return self._statistics

    def extra_show(self) -> None:
        harvest_season = self.get_harvest_season()
        nutritional_value: int = self.get_nutritional_value()
        print(f"Harvest season: {harvest_season}")
        print(f"Nutritional value: {nutritional_value}kcal")


def show_statistics_plant(self) -> None:
    self.get_statistics().display()


if __name__ == "__main__":
    def ft_garden_analytics() -> None:
        print("============ Garden Plant Types ============")
        print("========= Flower")
        plant = Flower("Rose", 15, 10, "Red", False)
        plant.set_height(20)
        plant.set_age(1)
        plant.set_color("red")
        plant.show()
        show_statistics_plant(plant)
        plant.grow()
        plant.get_old()
        plant.set_bloom(True)
        plant.show()
        show_statistics_plant(plant)

        print("========= Tree")
        plant2 = Tree("Pine", 15, 10, 10, True)
        plant2.set_height(200)
        plant2.set_age(15)
        plant2.set_trunk_diameter(45)
        plant2.show()
        show_statistics_plant(plant2)
        plant2.show()
        plant2.produce_shade()
        show_statistics_plant(plant2)

        print("========= Vegetable")
        plant3 = Vegetable("Tomatoe", 15, 10, "april", 0)
        plant3.set_height(15)
        plant3.set_age(1)
        plant3.set_harvest_season("october")
        plant3.set_nutritional_value(0)
        plant3.show()
        show_statistics_plant(plant3)
        plant3.grow_vegetable()
        plant3.show()
        show_statistics_plant(plant3)

        print("========= Anonymous plant")
        plant_anon = Plant.create_anonymous()
        plant_anon.show()
        show_statistics_plant(plant_anon)

    ft_garden_analytics()
