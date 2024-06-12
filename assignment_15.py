# assignment 15 - choose car brand

cars: list[str] = ["Proton", "Perodua", "Ferrari", "Audi"]

print("Available cars are:")
for i, car in enumerate(cars):
    print(f"{i+1}. {car}")

try:
    choice: int = int(input("Choose a car: ").strip())
except ValueError:
    raise ValueError("Invalid choice number")

if not 0 < choice <= len(cars):
    print("You didn't key in correct number")
else:
    print(f"My favourite car brand is {cars[choice-1]}")
