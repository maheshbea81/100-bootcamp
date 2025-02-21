# Victoria
a = 10
b = 5
c = 2
d = 1
e = 8
f = False

# BIDMAS BODMAS
# Brackets Indices Division Multiplication Addition Subtraction
# PEMDAS - Parentheses Exponent Mult Div Add Subtract
calculation_result = a + b - c * d / e
print(calculation_result)

calculation_result = (a + b) - c * d / e
print(calculation_result)

calculation_result = a + (b - c) * d / e
print(calculation_result)

calculation_result = (a + (b - c)) * d / e
print(calculation_result)

calculation_result = (a + (b - c)) * (d / e)
print(calculation_result)

calculation_result = (a + b - c * d) / e
print(calculation_result)


print("~" * 60)

if a < 20 and b > 1 and not f:
    print("a is less than 20 and b is greater than 1 and f is False")

if not f and c == 2:
    print('f is False and c is 2')

if c == 2 and not f:
    print('f is False and c is 2')