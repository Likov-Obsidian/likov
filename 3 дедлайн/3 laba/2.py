def sum_digits(number):
    number = abs(number)

    if number < 10:
        return number

    last_digit = number % 10
    remaining_digits = number // 10
    
    return last_digit + sum_digits(remaining_digits)

print(sum_digits(12345))
print(sum_digits(0))
print(sum_digits(9))
print(sum_digits(-123))