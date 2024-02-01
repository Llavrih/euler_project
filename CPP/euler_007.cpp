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
    int num = 0;
    long long i = 1;
    while (true) {
        if (isPrime(i)) {
            num += 1;
        }
        if (num == 10001){
            cout << i << endl;
            break;
        }
        i++;
    }      
    return 0;
}
