from TemeratureConversion.CustomError import CustomError

def get_temperature(prompt):
    while True:
        try:
            temp = float(input(prompt))
            return temp
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_unit(prompt):
    while True:
        try:
            unit = input(prompt)
            if unit not in ["C", "F", "K"]:
                raise CustomError("Invalid unit. Please enter 'C', 'F', or 'K' only.")
            return unit
        except CustomError as e:
            print(e)

def convert_unit(temp, unit, to_unit) -> float:
    if unit == to_unit:
        return temp
    elif unit=="K":
        if to_unit=="C":
            return temp-273.15
        else:
            return temp * 9/5 - 459.67
    elif unit=="C":
        if to_unit=="K":
            return temp+273.15
        else:
            return temp*9/5+32
    else:
        if to_unit=="C":
            return (temp-32)*5/9
        else:
            return (temp-32)/1.8 +273.15

# Get temperature input
temp = get_temperature("Enter temperature you want to convert: ")

# Get a valid initial unit
unit = get_valid_unit("Enter the unit (C/F/K): ")

# Get a valid target unit
to_unit = get_valid_unit("Enter the unit to which you want to convert (C/F/K): ")

print(f"Converted temperature is {round(convert_unit(temp,unit,to_unit),2)} {to_unit}")