
diploma_program: dict[str, str] = {
    "Z": "Diploma in Computer Science",
    "W": "Diploma in Management Technology (Accounting)",
    "F": "Diploma in Property Management",
    "Q": "Diploma in Quantity Surveying",
    "G": "Diploma in Management Technology"
}

choice: str = input("Please choose a diploma program: ").strip().upper()
if choice in diploma_program.keys():
    print(f"You are enrolled in {diploma_program[choice]}")
else:
    print("You are not taking any diploma program")
