class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height) -> None:
        if height >= 0:
            self._height: float = height
        else:
            print("Height can't be negative")

    def set_age(self, age) -> None:
        if age >= 0:
            self._age: int = age
        else:
            print("Age can't be negative")
        

    def is_more_than_year(days: int) -> None:
        if days > 365:
            print(f"Is {days} more than a year (365)? -> True")
        else:
            print(f"Is {days} more than a year (365)? -> False")





Plant.is_more_than_year = staticmethod(Plant.is_more_than_year)


if __name__ == "__main__":
    def ft_garden_analytics() -> None:
        
        Plant.is_more_than_year(366)
        Plant.is_more_than_year(364)
        Plant.is_more_than_year(365)
        Plant.is_more_than_year(0)
        Plant.is_more_than_year(-364)
        Plant.is_more_than_year(-365)
        Plant.is_more_than_year(-366)
    
    ft_garden_analytics()