def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    except ValueError:
        print("Invalid input! Please enter a valid number for the temperature.")
        return None
    finally:
        print("Thank you for using the weather forecast application.")
def main():
    user_input = input("Enter the temperature in Fahrenheit: ")
    celsius = fahrenheit_to_celsius(user_input)
    if celsius is not None:
        print(f"{user_input} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
if __name__ == "__main__":
    main()
