#include <iostream>
#include <cmath>

using namespace std;

int countDivisors(int n) {
    int count = 0;
    for (int i = 1; i <= sqrt(n); i++) {
        if (n % i == 0) {
            if (n / i == i) {
                count++;
            } else {
                count += 2;
            }
        }
    }
    return count;
}

int findTriangleNumber(int divisorLimit) {
    int n = 1;         
    int triangleNumber = 1;  

    while (countDivisors(triangleNumber) <= divisorLimit) {
        n++;
        triangleNumber += n;  
    }

    return triangleNumber;
}

int main() {
    int divisorLimit = 500;
    cout << "The first triangle number to have over " << divisorLimit << " divisors is: " 
              << findTriangleNumber(divisorLimit) << endl;

    return 0;
}
