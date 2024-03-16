def is_s_number(n):
    root = int(n**0.5)
    if root * root != n:
        return False  

    str_n = str(n)

    def check_splits(index, current_sum):
        if index == len(str_n):
            return current_sum == root
        for i in range(index + 1, len(str_n) + 1):
            segment = int(str_n[index:i])
            if check_splits(i, current_sum + segment):
                return True
        return False

    return check_splits(0, 0)

def T(N):
    limit = int(N**0.5) + 1
    return sum(n*n for n in range(1, limit) if is_s_number(n*n))

print(T(10**12)-1)  
