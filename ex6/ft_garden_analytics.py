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


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

    def bloom(self) -> None:
        print(f"{self.name} has not bloomed yet")
        print("[asking the rose to bloom]")
        self.show()
        print(f"{self.name} is blooming beautifully!")

    class nested():


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
        print()
        print()


def ft_show_stats() -> None:
    print(f"[statistics for {self.name}]")
    print(f"Stats: {} grow, {} age, {} show")
    

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
