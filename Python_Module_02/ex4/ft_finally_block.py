class GardenError(Exception):
    def __init__(self, message: str = "Garden error detected") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Plant error detected") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    check_caps: str = str.capitalize(plant_name)
    if plant_name == check_caps:
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Error: {plant_name} "
                         "first letter is not capitalized\n")


def test_watering_system() -> None:
    print("Opening watering system")
    caps_plants: list = ["Lettuce", "Tomatoe", "Potatoe", "onion", "Carrot"]
    print("Testing plants")
    try:
        for plant in caps_plants:
            water_plant(plant)
    except PlantError as error:
        print(f"{error}")
        return
    finally:
        print("Closing watering system")
        print("All clean and pretty!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
