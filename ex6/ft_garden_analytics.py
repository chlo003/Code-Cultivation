class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.day = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.day} days old")

    @staticmethod
    def check(age) -> bool:
        return age > 365

    @classmethod
    def create(cls) -> Plant:
        return cls("Unknown plant", 0.0, 0)

    class statistic():
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


def show_stats() -> None:
   print() 
#    print(f"[statistics for {self.name}]")
#    print(f"Stats: {} grow, {} age, {} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

    def bloom(self) -> None:
        print(f"{self.name} has not bloomed yet")
        print("[asking the rose to grow and bloom]")
        self.show()
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)

    def show(self) -> None:
        super().show()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    
    show_stats()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print()
    print("=== Anonymous")
    Plant.create()
    Plant.show(Plant.create())
    show_stats()

#to do list : changer bloom