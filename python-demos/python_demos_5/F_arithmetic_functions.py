# add function
def add(number1, number2):
    answer = int(number1) + int(number2)
    return answer


# subtract function
def subtract(number1, number2):
    answer = int(number1) - int(number2)
    return answer


# variadic add function
def add_many(*numbers):
    answer = 0
    for number in numbers:
        answer += int(number)
    return answer


def do_magic(number1, number2):
    number1_squared = number1 * number1
    number2_doubled = number2 * 2
    return number1_squared, number2_doubled
