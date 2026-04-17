def ft_water_reminder() -> None:
    last_time_watered: int = int(input("Days since last watering: "))
    if last_time_watered > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
