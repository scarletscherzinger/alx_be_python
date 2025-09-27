# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Function to get temperature input and raise ValueError if invalid
def get_temperature_input():
    try:
        return float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Function to get unit input (C or F) and raise ValueError if invalid
def get_unit_input():
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit not in ('C', 'F'):
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
    return unit

# Main function to orchestrate conversion
def main():
    temperature = get_temperature_input()
    unit = get_unit_input()

    if unit == 'C':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    else:  # unit == 'F'
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")

if __name__ == "__main__":
    main()
