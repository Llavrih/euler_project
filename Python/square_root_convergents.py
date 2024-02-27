from fractions import Fraction

def count_expansions(limit):
    count = 0
    fraction = Fraction(1, 2)  
    
    for _ in range(limit):
        fraction = 1 / (2 + fraction)  
        expansion = 1 + fraction  
        
        if len(str(expansion.numerator)) > len(str(expansion.denominator)):
            count += 1
    
    return count


print(count_expansions(1000))



