import numpy as np

number_sequence = "".join(str(i) for i in range(1, 200000))
number_sequence_int = int(number_sequence)
print(len(number_sequence))
print(
    int(number_sequence[0])
    * int(number_sequence[10 - 1])
    * int(number_sequence[100 - 1])
    * int(number_sequence[1000 - 1])
    * int(number_sequence[10000 - 1])
    * int(number_sequence[100000 - 1])
    * int(number_sequence[1000000 - 1])
)
