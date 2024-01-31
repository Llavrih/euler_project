#include <iostream>
using namespace std;

long long reverseNumber(long long n) {
    long long reversed = 0;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    return reversed;
}

bool isPalindrome(long long n) {
    if (n < 0) return false;
    return n == reverseNumber(n);
}

int main() {
    long long largestPalindrome = 0;

    for (long long i = 1000; i > 900; i--){
        for (long long j = 1000; j > 900; j--){
            long long num = i * j;
            if (isPalindrome(num) && num > largestPalindrome) {
                largestPalindrome = num;
                break;
            }
        }
    }

    if (largestPalindrome > 0) {
        cout << largestPalindrome << " is the largest palindrome." << endl;
    } else {
        cout << "No palindrome found." << endl;
    }
    
    return 0;
}
