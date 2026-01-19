from datetime import date


def calculate_age(year: int, month: int, day: int) -> str:
    """
    Calculate age in years, months, and days based on birth date.
    """
    try:
        birth_date = date(year, month, day)
    except ValueError:
        return "Invalid date. Please enter a valid birth date."

    today = date.today()

    if birth_date > today:
        return "Birth date cannot be in the future."

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += 30  # Approximation for simplicity

    if months < 0:
        years -= 1
        months += 12

    return f"Your age is {years} years, {months} months, {days} days"


def main():
    try:
        year = int(input("Enter your birth year: "))
        month = int(input("Enter your birth month: "))
        day = int(input("Enter your birth day: "))

        result = calculate_age(year, month, day)
        print(result)

    except ValueError:
        print("Please enter numeric values only.")


if __name__ == "__main__":
    main()