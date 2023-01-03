#include <iostream>

using namespace std;

void init() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}
void solve() {
    int N, max, sum;
    double avg;
    max = 0;
    sum = 0;
    cin >> N;

    int array[1000];
    int arrayn[1000];

    for(int i = 0; i < N; i++){
        cin >> array[i];
        if(max < array[i]) max = array[i];
    }   

    for(int i = 0; i < N; i++){
        arrayn[i] = (array[i] * 100) / max;
        sum += arrayn[i];
    }
    avg = (double)sum / (double)N;
    cout << avg;
}

int main() {
    init();
    solve();
}