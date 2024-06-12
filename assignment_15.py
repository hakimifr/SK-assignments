# assignment 15 - choose car brand

cars: list[str] = ["Proton", "Perodua", "Ferrari", "Audi"]

print("Available cars are:")
for i, car in enumerate(cars):
    print(f"{i+1}. {car}")

choice: str = input("Choose a car: ")
if choice.strip() not in cars:
    raise ValueError("Invalid car chosen!")

print(f"My favourite car brand is: {choice.strip()}")
