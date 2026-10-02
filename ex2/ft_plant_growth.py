class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
       self.height = self.height + 0.8

    def old(self) -> None:
        self.age = self.age + 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    rose.show()
    tall =  rose.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.old()
        rose.show()
    print(f"Growth this week: {round(rose.height - tall, 1)}cm")
  