#include <iostream>

using namespace std;

void init() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
}
void solve() {
    int array[9];
    int maxth;
    int count = 0;
    int max = 0;

    for(int i = 0; i < 9; i++){
        cin >> array[i];
        count++;

        if(max < array[i]){
        max = array[i];
        }
    }

    for(int i = 0; i < 9; i++)
    {
        if(max == array[i]){
            maxth = i + 1;
        }
    }

    cout << max << "\n" << maxth;
}

int main() {
	init();
	solve();
}