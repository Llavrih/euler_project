#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(long long n) {
    if (n <= 1) return false;
    for (long long i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    long long num = 600851475143LL;
    for (long long i = sqrt(num); i >= 2; i--) {
        if (num % i == 0 && isPrime(i)) {
            cout << i << " ";
        }
    }      
    return 0;
}
