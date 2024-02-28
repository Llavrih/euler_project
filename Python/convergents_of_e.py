def e_sequence(n):
    seq = [2]
    k = 1
    while len(seq) < n:
        seq.extend([1, 2*k, 1])
        k += 1
    return seq[:n]

def sum_digits_nth_convergent(n):
    seq = e_sequence(n)
    p_n_minus_2, p_n_minus_1 = 1, seq[0]
    q_n_minus_2, q_n_minus_1 = 0, 1

    for i in range(2, n + 1):
        a_n = seq[i-1]
        p_n = a_n * p_n_minus_1 + p_n_minus_2
        q_n = a_n * q_n_minus_1 + q_n_minus_2

        p_n_minus_2, p_n_minus_1 = p_n_minus_1, p_n
        q_n_minus_2, q_n_minus_1 = q_n_minus_1, q_n

    return sum(int(digit) for digit in str(p_n))

sum_digits_100th = sum_digits_nth_convergent(100)
print(sum_digits_100th)
