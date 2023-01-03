#include <iostream>
#include <string>

using namespace std;

void init() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

void solve() {
    long long number;
    cin >> number;
    int counter = 1;
    long long range = 1;
    long long tmp = 1;

    while(1){
        if(range >= number){
            break;
        }
        tmp = 6*(counter++);
        range += tmp;
    }   

    cout << counter;
}

int main() {
    init();
    solve();
}