class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.__name = name
        self.__height = height
        self.__age = age

    def show(self) -> str:
        return (f"{self.__name}: {round(self.__height, 1)}cm, "
                f"{self.__age} days old")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{rose.__name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.__height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{rose.__name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.__age = age

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: {rose.show()}")
    print()
    rose.set_height(25)
    rose.set_age(30)
    print(f"Height updated: {rose.get_height()}cm")
    print(f"Age updated: {rose.get_age()} days")
    print()
    rose.set_height(-25.0)
    rose.set_age(-30)
    print()
    print(f"Current State: {rose.show()}")
