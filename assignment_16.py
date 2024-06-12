# Assignment 16 - Choose food menu

foods: list[str] = ["spaghetti", "pizza", "burger", "makaroni"]

for i, food in enumerate(foods):
    print(f"{i}. {food.strip().capitalize()}")

choice: str = input("Please choose your menu: ")
if choice.lower() in foods:
    print(f"You have ordered {choice.capitalize()}")
else:
    raise ValueError("Invalid food selected!")
