# Assignment 20 - Choose club

clubs: dict[str, str] = {
    "C": "Computer Club",
    "A": "Art Club",
    "S": "Science Club",
    "L": "Language Club"
}

choice: str = input("Choose a club: ").strip().upper()

if choice in clubs.keys():
    print(f"You are taking {clubs[choice]}")
else:
    print("You are not taking any club")
