#include <iostream>

using namespace std;

void init() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
}
void solve() {
	int test, a ,b;
	int pc;
	int data = 1;
	cin >> test;
	for (int i = 0; i < test; i++) {
		cin >> a >> b;
		for (int j = 0; j < b; j++) {
			data = data * a;
		}
		pc = data % 10;
		cout << pc;
	}
}
int main() {
	init();
	solve();
}