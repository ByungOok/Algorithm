#include <iostream>

using namespace std;


void init() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
}


void solve() {
	int n, result;
    int bit = 1;
    result = 0;
    cin >> n;


    if(n == 0)
    result = 0;
    else if(n < 2)
    result = 1;
    else
    {
        while(bit <= n)
        {
            result++;
            bit *= 2;
        }
    }
    cout << result;   

}


int main() {
	init();
	solve();
}