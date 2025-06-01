import math

class Greeter:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self, times: int = 1) -> None:
        for i in range(times):
            print(f"Hello, {self.name}!")

def main():
    try:
        name = input("Enter your name: ")
        greeter = Greeter(((name)))
        greeter.greet(times=3)

        numbers = [1, 2, 3, 4, 5]
        squares = [x**2 for x in numbers]
        print("Squares:", squares)

        my_dict = {"a": 1, "b": 2, "c": 3}
        for key, value in my_dict.items():
            print(f"{key} -> {math.sqrt(value):.3f}")

    except ValueError as e:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
