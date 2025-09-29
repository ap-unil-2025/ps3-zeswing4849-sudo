"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    # TODO: Implement this function
    return(celsius*9/5)+32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    # TODO: Implement this function
    return((fahrenheit-32)*5/9)


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    # TODO: Implement the interactive converter
    # Remember to:
    # - Get temperature value from user
    # - Get unit (C or F) from user
    # - Validate input
    # - Perform conversion
    # - Display result rounded to 2 decimal places
        # Get temperature value from user
    
    temp = float(input("Enter temperature : "))
    
    
    # Get unit (C or F) from user
    unit = input("Enter unit (C for Celsius, F for Fahrenheit) : ").upper()
    
    # Validate input
    if unit not in ['C', 'F']:
        print("Error : 'C' or 'F' only !")
        return
    
    # Perform conversion
    if unit == 'C':
        # Convert Celsius to Fahrenheit
        result = (temp * 9/5) + 32
        print(f"{temp}°C = {result:.2f}°F")
    else:
        # Convert Fahrenheit to Celsius
        result = (temp - 32) * 5/9
        print(f"{temp}°F = {result:.2f}°C")


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()