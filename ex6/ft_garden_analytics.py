class Plant:
    class Statistic():
        def __init__(self):
            self.stat_grow = 0
            self.stat_age = 0
            self.stat_show = 0

        def hold_data_grow(self):
            self.stat_grow = self.stat_grow + 1

        def hold_data_age(self):
            self.stat_age = self.stat_age + 1

        def hold_data_show(self):
            self.stat_show = self.stat_show + 1


    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.day = age
        self.stats = self.Statistic()
    
    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.day} days old")
        self.stats.hold_data_show()

    def grow(self, tall : float)-> None:
        self.height = self.height + tall
        self.stats.hold_data_grow()

    def age(self, old: int) -> None:
        self.day = self.day + old
        self.stats.hold_data_age()

    @staticmethod
    def check(age) -> bool:
        return age > 365

    @classmethod
    def create(cls) -> Plant:
        return cls("Unknown plant", 0.0, 0)


def show_stats(plant: Plant) -> None:
    print(f"[statistics for {plant. name}]")
    print(f"Stats: {plant.stats.stat_grow} grow, {plant.stats.stat_age} age, {plant.stats.stat_show} show")
        


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        print(f"{self.name} has not bloom yet")

    def bloom(self) -> None:
        print("[asking the rose to grow and bloom]")
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    class Statistic(Plant.Statistic):
        def __init__(self):
            super().__init__()
            self.stat_shade = 0

        def hold_data_shade(self):
            self.stat_shade = self.stat_shade + 1
        
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print(f"Tree Oak now produces a shade of {self.height}cm long and "
              f"{self.trunk_diameter}cm wide")
        self.Stat_Tree().stat_shade
        

class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)

    def show(self) -> None:
        super().show()
        if self.bloom():
            print("Seeds: 42")
        else:
            print("Seeds: 0")

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check(400)}")
    print()
    
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_stats(rose)
    rose. grow(8)
    rose.bloom()
    rose.show()
    show_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_stats(oak)
    
    show_stats(oak)
    print()
            
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print()
    
    
    
    
    print("=== Anonymous")
    Plant.create()
    Plant.show(Plant.create())

#to do list : changer bloom