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

int multiples_5() {
    int sum = 0;
    for (int i = 0; i < 1000; i++) {
        if ((i%5==0) && !(i%3==0)){
            sum += i;
        };
    };
    return sum;
}

int main() {
    int sum = 0;
    sum = multiples_3() + multiples_5();

    cout << "Sum = " << sum;    
        
    return 0;
}