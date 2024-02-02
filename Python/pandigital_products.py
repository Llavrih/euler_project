def is_pandigital(n):
    return sorted(n) == list("123456789")


def find_pandigital_products():
    products = set()
    for i in range(1, 100):
        for j in range(100, 10000 // i):
            prod = i * j
            concat_str = f"{i}{j}{prod}"
            if len(concat_str) > 9:
                break
            if is_pandigital(concat_str):
                products.add(prod)

    return sum(products), products


total_sum, unique_products = find_pandigital_products()
print(total_sum, unique_products)
