n = 1  
partitions = [1]  
modulus = 10**6  

def pentagonal_numbers(n):
    return n * (3 * n - 1) // 2

while True:
    i = 0
    pentagonal = 1
    partitions.append(0)  

    while pentagonal <= n:
        sign = -1 if i % 4 > 1 else 1 
        partitions[n] += sign * partitions[n - pentagonal]
        partitions[n] %= modulus  
        i += 1
        if i % 2 == 0:
            pentagonal = pentagonal_numbers(i // 2 + 1)
        else:
            pentagonal = pentagonal_numbers(-((i // 2) + 1))

    if partitions[n] == 0:  
        break

    n += 1

print(n)
