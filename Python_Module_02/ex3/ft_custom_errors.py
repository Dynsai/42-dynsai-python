class GardenError(Exception):
    def __init__(self, message: str = "Garden error detected") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Plant error detected") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Water error detected") -> None:
        super().__init__(message)


def custom_errors() -> None:
    try:
        print("Testing PlantError")
        raise PlantError("Onion plant is dead")
    except PlantError as error:
        print(f"Caught PlantError! {error}\n")
    try:
        print("Testing WaterError")
        raise WaterError("Plant need water to grow")
    except WaterError as error:
        print(f"Caught WaterError! {error}\n")
    print("Testing catching all errors...")
    try:
        raise PlantError()
    except GardenError as error:
        print(f"Caught GardenError! {error}")
    try:
        raise WaterError()
    except GardenError as error:
        print(f"Caught GardenError! {error}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    custom_errors()
    print("=== End of Custom Garden Errors Demo ===")
