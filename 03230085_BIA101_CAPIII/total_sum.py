#03230085
#Jigme Sherab
#BBI 'A'

#References
#https://youtu.be/9BsdhBoTvKU?si=7lyX6I-XyprvPbFl


# importing file using opearting system
import os

# go through each f character in the input string
def extract_digits_from_line(line):
    first_digit = None
    last_digit = None

    # Find the first and last digits in the line
    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char  # Update last_digit every time a digit is encountered

    # Form the two-digit number from the first and last digits found
    if first_digit is not None and last_digit is not None:
        
        return int(first_digit + last_digit)
    else:
        return 0

def process_file(file_path):
    total_sum = 0

    try:
        with open(file_path, 'r') as file:  # Open the file in read mode
            for line in file:
                two_digit_number = extract_digits_from_line(line)
                total_sum += two_digit_number

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred while processing the file '{file_path}': {e}")
        return 0

    return total_sum

# Get the input file path based on the last three index numbers
index = "085"
file_name = f"{index}.txt"
input_file_path = os.path.join(r'C:\Users\user\Desktop\BIA101_CAPIII\03230085_BIA101_CAPIII', file_name)

if os.path.isfile(input_file_path):
    # Calculate the result by processing the input file
    result = process_file(input_file_path)
    print(result)
else:
    print(f"Error: The input file '{file_name}' was not found.")