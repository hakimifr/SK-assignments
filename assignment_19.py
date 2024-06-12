# Assignment 19 - Choose subject

subjects: list[str] = ["Account Principle", "Biology", "Art"]

for i, sub in enumerate(subjects):
    print(f"{i+1}. {sub}")

try:
    choice: int = int(input("Choose a subject: ").strip())
except ValueError:
    print("Not a valid choice number!")

if not 0 < choice <= len(subjects):
    print("You are not taking any subject")
else:
    print(f"You are taking {subjects[choice-1]}")
