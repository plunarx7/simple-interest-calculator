# calculate_interest.py

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    Args:
        principal (float): The principal amount.
        rate (float): The annual interest rate (in percentage).
        time (float): The time period in years.

    Returns:
        float: The interest accrued over the period.
    """
    return (principal * rate * time) / 100

def main():
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (in %): "))
        time = float(input("Enter the time in years: "))
        interest = calculate_simple_interest(principal, rate, time)
        print(f"Simple interest: {interest:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
