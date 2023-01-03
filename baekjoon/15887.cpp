#include <iostream>

using namespace std;


void init() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
}


void solve() {
	int number, card[1000];
	cin >> number;
	for (int i = 0; i <number; i++)
	{
		cin >> card[i];
	}

	int count = 0;
	int a[1000], b[1000];
	for (int i = 0; i < number; i++)
	{
		for (int j = i; j < number; j++)
		{
			if (card[j] > card[j+1])
			{
				int temp;
				temp = card[i];
				card[i] = card[j];
				card[i] = temp;
				a[count] = i, b[count] = j;
				count++;				
			}
		}
	}
	printf("%d \n", count);
	for (int i = 0; i < count; i++)
	{
		printf("%d %d \n", a[i], b[i]);
	}
}


int main() {
	init();
	solve();
}