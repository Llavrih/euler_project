#include <iostream>
#include <cmath>

int main() {
    int count = 0;

    
    for (int n = 1; n < 22; ++n) { 
        for (int b = 1; b < 10; ++b) { 
            double power = pow(b, n);
            int digits = floor(log10(power)) + 1; 
            if (digits == n) {
                ++count;
            }
        }
    }

    std::cout << "Total count: " << count << std::endl;
    return 0;
}
