max_solutions = 0
p_with_max_solutions = 0

for p in range(12, 1001):
    solutions = 0
    for a in range(1, p // 3):
        b = (p * p - 2 * p * a) / (2 * p - 2 * a)
        if b.is_integer() and b > a:
            c = p - a - b
            if c > b:
                solutions += 1
    if solutions > max_solutions:
        max_solutions = solutions
        p_with_max_solutions = p


print(p_with_max_solutions, max_solutions)
