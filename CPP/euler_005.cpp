#include <iostream>
using namespace std;

long long greatestCommonDivisor(long long a, long long b) {
    if (b == 0) 
        return a;
    return greatestCommonDivisor(b, a % b);
}

long long leastCommonMultiple(long long a, long long b) {
    return (a / greatestCommonDivisor(a, b)) * b;
}

int main() {
    long long result = 1;
    for (long long i = 2; i <= 20; i++) {
        result = leastCommonMultiple(result, i);
    }
    cout << result << endl;
    return 0;
}
