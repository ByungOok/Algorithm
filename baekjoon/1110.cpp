#include <iostream>

using namespace std;

void init() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
}
void solve() {
	int N, S, I, number, sum, next;
	int count = 0;

	cin >> N;

	number = N;

	do{
		S = number / 10;
		I = number % 10;

		sum = S + I;
		next = (I * 10) + (sum % 10);

		number = next;
		count++;

	}while(next != N);

	cout << count;
}

int main() {
	init();
	solve();
}