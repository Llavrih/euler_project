#include <iostream>
using namespace std;

int evenFibonacci() {
    int sum = 0;
    int f = 1;
    int t2 = 1;
    int t1 = 0;
    
    while (f < 4000000) {      
        f = t1 + t2;
        t1 = t2;
        t2 = f;
        if (f%2==0){
            sum += f;
        };
        
    };
    return sum;
}

int main() {
    int sum = 0;
    sum = evenFibonacci();

    cout << "Sum = " << sum;    
        
    return 0;
}