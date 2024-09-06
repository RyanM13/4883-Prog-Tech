/**
* Name: Ryan Mathews
* Course: 4883 Prog-tech
* Date: 9/6/2024
*/
#include <iostream> 

#define endl "\n"

using namespace std;

int main() {
    long B = 0, A = 0;

    while (cin >> A >> B) {

        // your stuff here
        if(A > B){
            cout << A - B <<"\n";
        }
        else{
            cout << B - A << "\n";
        }

    }
    return 0;
}
