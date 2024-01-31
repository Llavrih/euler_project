#include <iostream>
using namespace std;

int multiples_3() {
    int sum = 0;
    for (int i = 0; i < 1000; i++) {
        if (i%3==0){
            sum += i;
        };
    };
    return sum;
}

int even_fibonacci() {
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
    sum = even_fibonacci();

    cout << "Sum = " << sum;    
        
    return 0;
}