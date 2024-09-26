def convert_length(value, from_unit, to_unit):
    length_units = {'meters': 1, 'kilometers': 0.001, 'centimeters': 100, 'millimeters': 1000, 'miles': 0.000621371, 'feet': 3.28084, 'inches': 39.3701}
    
    if from_unit in length_units and to_unit in length_units:
        return value * length_units[to_unit] / length_units[from_unit]
    else:
        return "Invalid length units!"

def convert_weight(value, from_unit, to_unit):
    weight_units = {'grams': 1, 'kilograms': 0.001, 'pounds': 0.00220462, 'ounces': 0.035274}
    
    if from_unit in weight_units and to_unit in weight_units:
        return value * weight_units[to_unit] / weight_units[from_unit]
    else:
        return "Invalid weight units!"

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    else:
        return "Invalid temperature units!"

def unit_converter():
    print("Unit Converter")
    print("--------------")
    print("Choose conversion type:")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        value = float(input("Enter value: "))
        from_unit = input("Enter the unit you're converting from (e.g., meters, kilometers, feet): ").lower()
        to_unit = input("Enter the unit you're converting to (e.g., miles, inches, centimeters): ").lower()
        result = convert_length(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")

    elif choice == '2':
        value = float(input("Enter value: "))
        from_unit = input("Enter the unit you're converting from (e.g., grams, kilograms, pounds): ").lower()
        to_unit = input("Enter the unit you're converting to (e.g., ounces, pounds, kilograms): ").lower()
        result = convert_weight(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")

    elif choice == '3':
        value = float(input("Enter temperature value: "))
        from_unit = input("Enter the unit you're converting from (Celsius, Fahrenheit, Kelvin): ").capitalize()
        to_unit = input("Enter the unit you're converting to (Celsius, Fahrenheit, Kelvin): ").capitalize()
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    unit_converter()
