
edu_level: dict[str, str] = {
    "f": "foundation",
    "d": "diploma",
    "b": "bachelor degree",
    "m": "master"
}

for letter, edlevel in edu_level.items():
    print(f"{letter}. {edlevel}")

choice: str = input("Please choose course: ").strip().lower()

if choice in edu_level.keys():
    print(edu_level[choice])
else:
    raise ValueError("Course does not exist!")
