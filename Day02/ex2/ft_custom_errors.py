class GardenError(Exception):
    def __init__(self) -> None:
        self.message = "Caught PlantError: The tomato plant is wilting!"
        self.message1 = "Caught WaterError: Not enough water in the tank!"
        pass


class PlantError(GardenError):
    def __init__(self) -> None:
        self.message = "Caught PlantError: The tomato plant is wilting!"
        pass


class WaterError(GardenError):
    def __init__(self) -> None:
        self.message = "Caught WaterError: Not enough water in the tank!"
        pass


def do_error(percentage_of_well_being: int, percentage_of_water: int,
             i: int) -> None:
    if i == 1:
        print("=== Custom Garden Errors Demo ===\n")

        print("Testing PlantError...")
    try:
        if int(percentage_of_well_being) < 75:
            raise PlantError
    except ValueError:
        print("Caught ValueError: invalid literal for int()", "\n")
        return
    except PlantError as e:
        print(e.message)
    if i == 1:
        print
        print("Testing WaterError...")
    try:
        if int(percentage_of_water) < 75:
            raise WaterError
    except ValueError:
        print("Caught ValueError: invalid literal for int()", "\n")
        return
    except WaterError as e:
        print(e.message, "\n")
    if i == 1:
        print("Testing catching all garden errors...")
    i += 1
    if (i <= 2):
        do_error(percentage_of_well_being, percentage_of_water, i)


if __name__ == "__main__":
    do_error(5, "5", 1)
