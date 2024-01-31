import numpy


def find_cycle(numerator, denominator):
    remainder = numerator % denominator
    seen = {}
    cycle = ""

    while remainder != 0 and remainder not in seen:
        seen[remainder] = len(cycle)
        remainder *= 10
        cycle_digit, remainder = divmod(remainder, denominator)
        cycle += str(cycle_digit)

    if remainder == 0:
        return None  # No cycle
    else:
        start = seen[remainder]
        return cycle[start:]  # Cycle found


biggest_len = 0
int_len = 0
for d in range(1, 1000):
    if find_cycle(1, d) != None:
        if len(find_cycle(1, d)) > biggest_len:
            biggest_len = len(find_cycle(1, d))
            int_len = d
print(biggest_len, int_len)
