"""Simple Student Grade Manager"""

students = {}  # name -> mark


def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name.lower() in (n.lower() for n in students):
        print(f"'{name}' already exists. Duplicate names are not allowed.")
        return

    text = input("Mark (0-100): ").strip()
    try:
        mark = float(text)
    except ValueError:
        print("Invalid mark. Please enter a number.")
        return
    if mark < 0 or mark > 100:
        print("Mark must be between 0 and 100.")
        return

    students[name] = mark
    print(f"Added {name} with mark {mark:g}.")


def show_students():
    if not students:
        print("No students added yet.")
        return

    print()
    print(f"{'Name':<20}{'Mark':>8}{'Grade':>8}")
    print("-" * 36)
    for name, mark in students.items():
        print(f"{name:<20}{mark:>8.1f}{get_grade(mark):>8}")
    print("-" * 36)

    marks = list(students.values())
    print(f"Class average : {sum(marks) / len(marks):.2f}")
    print(f"Highest mark  : {max(marks):g}")
    print(f"Lowest mark   : {min(marks):g}")


def main():
    while True:
        print("\n1. Add student\n2. Show results\n3. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
