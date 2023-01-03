#include <iostream>

using namespace std;

void init() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
}
void solve() {
    int N;

    int min = 1000000;
    int max = -1000000;

    cin >> N;
    int array[100];

    for(int i = 0; i < N; i++){
        cin >> array[i];
        if( max < array[i]) max = array[i];
        if( min > array[i]) min = array[i];
    }

    cout << min << " " << max;
}

int main() {
	init();
	solve();
}