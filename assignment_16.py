# Assignment 16 - Choose food menu

foods: list[str] = ["spaghetti", "pizza", "burger", "makaroni"]

for i, food in enumerate(foods):
    print(f"{i+1}. {food.strip().capitalize()}")

try:
    choice: int = int(input("Please choose your menu: ").strip())
except ValueError:
    raise ValueError("Not a number!")

if not 0 < choice <= len(foods):
    print("You didn't key in correct number")
else:
    print(f"You have ordered {foods[choice-1]}")
