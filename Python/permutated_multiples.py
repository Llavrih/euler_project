def all_digits_same(num1, num2):
    """
    Check if all digits in two numbers are the same.

    Args:
    num1 (int): The first number.
    num2 (int): The second number.

    Returns:
    bool: True if all digits are the same, False otherwise.
    """
    # Convert numbers to sets of their digits
    digits_num1 = set(str(num1))
    digits_num2 = set(str(num2))

    # Check if all digits are the same
    return digits_num1 == digits_num2


for i in range(1, 1000000):
    if all_digits_same(i, 2 * i) is True:
        print(all_digits_same(i, 2 * i), i, i * 2)
        if all_digits_same(i, 3 * i) is True:
            print(all_digits_same(i, 3 * i), i, i * 3)
            if all_digits_same(i, 4 * i) is True:
                print(all_digits_same(i, 4 * i), i, i * 4)
                if all_digits_same(i, 5 * i) is True:
                    print(all_digits_same(i, 5 * i), i, i * 5)
                    if all_digits_same(i, 6 * i) is True:
                        print(all_digits_same(i, 6 * i), i, i * 6)
                        print(i)
                        break
