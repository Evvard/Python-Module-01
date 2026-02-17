class Plant:

    def __init__(self, plant_name: str, size: int) -> None:
        self.plant_name = plant_name
        self.size = size

    def grow(self, add_size: int) -> None:
        i = add_size - self.size
        self.size = add_size
        print(f"{self.plant_name} gree {i}cm")

    def __str__(self) -> str:
        return f"- {self.plant_name}: {self.size}cm"


class FloweringPlant(Plant):

    def __init__(self, plant_name: str, size: int, color: str) -> None:
        super().__init__(plant_name=plant_name, size=size)
        self.color = color

    def __str__(self) -> str:
        base_text = super().__str__()
        return f"{base_text}, {self.color} flowers"


class PrizeFlower(FloweringPlant):

    def __init__(self, plant_name: str, size: int,
                 color: str, prize: str) -> None:
        super().__init__(plant_name=plant_name, size=size, color=color)
        self.prize = prize

    def __str__(self) -> str:
        base_text = super().__str__()
        return f"{base_text}, Prize points: {self.prize}"


class GardenManager:

    nombre_of_user = 0

    def __init__(self, username: str) -> None:
        self.user_name = username
        self.plants = []
        GardenManager.nombre_of_user += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)

    @classmethod
    def create_garden_network(cls):
        return cls.nombre_of_user

    class GardenStats:
        
        @staticmethod
        def validate_height(size: int) -> bool:
            if size > 0:
                return 1
            else:
                return 0

        @staticmethod
        def summarize_plants(plants: list) -> str:
            count = len(plants)
            for p in plants:
                total_growth += p.size
            return f"Plants added: {count}, Total growth: {total_growth}cm"
















if __name__ == "__main__":
    Oak_Tree = Plant("Oak Tree", 101)
    Rose = FloweringPlant("Rose", 26, "red")
    Sunflower = PrizeFlower("Sunflower", 51, "yellow", 10)
    print("=== Garden Management System Demo ===")








    print("Alice is helping all plants grow...")



        print(f"{self.plant_name} gree {i}cm, {self.color} flowers(), Prize points: {self.prize}")
        print(f"{self.plant_name} gree {i}cm, {self.color} flowers (NNNNNNNNN)")

    print("=== Alice's Garden Report ===")