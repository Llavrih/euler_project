def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    return n + int(str(n)[::-1])

def is_lychrel(n, max_iterations=50):
    for _ in range(max_iterations):
        n = reverse_and_add(n)
        if is_palindrome(n):
            return False
    return True

lychrel_count = sum(is_lychrel(i) for i in range(1, 10000))

print(lychrel_count)
