def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    
    main_digits = isbn[:length - 1]
    given_check_digit = isbn[length - 1]
    
    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print("Invalid character was found.")
        return
    
    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    elif length == 13:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    else:
        print("Length should be 10 or 13.")
        return
    # Compare check digits (handle X case)
    if given_check_digit.upper() == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')
        
def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)
    
def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit
def main():
    user_input = input('Enter ISBN and length: ')
    values = user_input.split(',')
    isbn = values[0]
    length = int(values[1])
    if length == 10 or length == 13:
    validate_isbn(isbn, length)
    else:
    print('Length should be 10 or 13.')

main()