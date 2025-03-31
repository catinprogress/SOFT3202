def delete_char(text, char_to_delete):
    if not isinstance(text, str):
        return "Input must be a string"

    count = 0
    result = ''

    for char in text:
        if char == char_to_delete:
            count += 1
        else:
            result += char

    return count

delete_char("Hello World", "o")
delete_char(1, "0")


def print_data(zipcode, email):
    if len(zipcode) == 4 and (len(email) <= 100 and len(email) >= 8):
        if '.' not in email or '@' not in email:
            print("\nEmail must contain . and @ characters")
        else: 
            print(f"zipcode: {zipcode} \t \t Email: {email}")
    elif len(zipcode) != 4:
        print("\nInvalid zipcode")
    else:
        print("\nInvalid Email length")

print_data("1234", "112@gmail.com")
print_data("1234", "112@gmail")
print_data("0", "Hello")
print_data("1234", "Hello")

def classify_triangle(a, b, c):

    if 0 < a <= 100 and 0 < b <= 100 and 0 < c <= 100:
        if (a + b > c) and (b + c > a) and (c + a > b):
            a1 = (a**2 + b**2) / (c**2)
            a2 = (b**2 + c**2) / (a**2)
            a3 = (c**2 + a**2) / (b**2)

            if a1 < 1 or a2 < 1 or a3 < 1:
                print("Obtuse angled triangle")
            elif a1 == 1 or a2 == 1 or a3 == 1:
                print("Right angled triangle")
            else:
                print("Acute angled triangle")
        else:
            print("Invalid Triangle")
    else:
        print("Input values are out of range")

def classify_triangle_simple(a, b, c):
    if not (0 < a <= 100 and 0 < b <= 100 and 0 < c <= 100):
        print("Input values are out of range")
        return

    if not (a + b > c and b + c > a and c + a > b):
        print("Invalid Triangle")
        return

    squares = sorted([a**2, b**2, c**2])
    if squares[0] + squares[1] < squares[2]:
        print("Obtuse angled triangle")
    elif squares[0] + squares[1] == squares[2]:
        print("Right angled triangle")
    else:
        print("Acute angled triangle")

classify_triangle(-1, 0, 0)
classify_triangle(1, 2, 3)
classify_triangle(3, 4, 5)
classify_triangle(6, 7, 8)
classify_triangle(3, 4, 6)