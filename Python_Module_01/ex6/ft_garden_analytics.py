class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float
        self._age: int
        
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
    
    def info(self) -> None:
        name = self.get_name()
        height = self.get_height()
        age = self.get_age()
        print(f"{name} with {height}cm of height and {age} years old")
        
            
if __name__ == "__main__":
    def ft_garden_analytics() -> None:
        p1 = Plant("Rose", 12.2, 3)
        p1.info()

    ft_garden_analytics()
        