#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n, p;

void init() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}


void solve() {
    do{
    cin >> n >> p;
    int page[3];
    int count = 0;
    
    if(p % 2 == 1)
    {
        page[0] = p + 1;

        int center = n / 2;

        if(p > center)
        {
            page[1] = p - 2*(p-center);
            page[2] = page[1]++;
        }
        else
        {
            page[1] = p + 2*(center-p);
            page[2] = page[1]++;
        }
    }
    else
    {
        int new_p = p--;
        page[0] = new_p;

        int center = n / 2;

        if(new_p > center)
        {
            page[1] = new_p - 2*(new_p-center);
            page[2] = page[1]++;
        }
        else
        {
            page[1] = new_p + 2*(center-new_p);
            page[2] = page[1]++;
        }

    }
    sort (page, page+2);

    
    for(int i = 0; i < 3; i++)
    {
        cout << page[i] << " ";
    }

    } while (n == 0);
}

int main() {
    init();
    solve();
}