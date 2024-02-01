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
    long long num = 2000000LL;
    long long sum = 0;
    for (long long i = 1; i <= num; i++) {
        if (isPrime(i)) {
            sum += i;
        }
    } 
    cout << "Sum: " << sum << endl;    
    return 0;
}
