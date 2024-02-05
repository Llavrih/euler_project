#include <iostream>
#include <gmpxx.h>  
using namespace std;

int main() {
    mpz_class num; 
    mpz_ui_pow_ui(num.get_mpz_t(), 2, 1000); 

    string numStr = num.get_str();

    long long sum = 0;
    for (char digit : numStr) {
        sum += digit - '0'; 
    }

    cout << "Sum: " << sum << endl;
    
    return 0;
}
