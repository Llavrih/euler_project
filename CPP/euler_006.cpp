#include <iostream>
#include <cmath>
using namespace std;

int main() {
    long long sum_square = 0;
    long long sum = 0;
    for (long long i = 1; i <= 100; i++) {
        sum_square += pow(i, 2);
        sum += i;
    }
    cout << static_cast<long long>(pow(sum, 2)) - sum_square << endl;
    return 0;
}
