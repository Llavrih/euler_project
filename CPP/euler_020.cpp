#include <iostream>
#include <gmpxx.h> 

using namespace std;

mpz_class factorial(int n) {
    mpz_class result = 1;
    for (int i = 1; i <= n; ++i) {
        result *= i;
    }
    return result;
}

int main() {
    int num = 100;
    mpz_class fact = factorial(num); 
    mpz_class sum = 0;

    string factStr = fact.get_str();
    for (char& digit : factStr) {
        sum += digit - '0';
    }

    cout << "Sum: " << sum << endl;
    return 0;
}
