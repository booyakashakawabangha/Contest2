# include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int array[n];
    for (int idx = 0; idx < n; idx++) {
        cin >> array[idx];
    }
    sort(array, array + n);
    int cost = array[0] * (n - 1);
    for (int idx = 1; idx < n; idx++) {
        cost += array[idx] * (n - idx);
        cout << array[idx] << endl;
    }
    cout << cost;
    return 0;
}