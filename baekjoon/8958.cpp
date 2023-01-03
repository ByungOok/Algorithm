#include <iostream>
#include <string>
#include <math.h>

using namespace std;

void init() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

void solve() {
    long long n = 1; 
    while (n*log(n) < 86400000000)
    {
        n += 1;
    }
}

int main() {
    init();
    solve();
}