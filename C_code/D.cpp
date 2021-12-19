#include <iostream>
#include <bits/stdc++.h>
using namespace std;

multiset<int> rivals;
multiset<int>::iterator iter;

int find_highest(int arr[], int nteams, int Armanchik) {
    Armanchik += arr[nteams - 1];
    int Amanchik_team_rate = 1;
    for (int i = 1; i < nteams - 1; i++) {
        rivals.insert(arr[i]);
    }
    while (!rivals.empty()) {
        iter = rivals.end();
        iter--;
        int team_mate = *iter;
        rivals.erase(iter);
        iter = rivals.upper_bound(Armanchik - team_mate);
        if (iter == rivals.begin()) {
            Amanchik_team_rate++;
            iter = rivals.end();
            iter--;
            rivals.erase(iter);
            continue;
        }
        iter--;
        rivals.erase(iter);
    }
    return Amanchik_team_rate;
}

int find_lowest(int arr[], int nteams, int Armanchik)
{
    Armanchik += arr[1];
    int Amanchik_team_rate = 1;
    for (int i = 2; i < nteams; i++)
        rivals.insert(arr[i]);
    while (!rivals.empty())
    {
        int team_mate = *rivals.begin();
        rivals.erase(rivals.begin());
        iter = rivals.upper_bound(Armanchik - team_mate);
        if (iter == rivals.end()) {
            rivals.erase(rivals.begin());
        } else {
            rivals.erase(iter);
            Amanchik_team_rate++;
        }
    }
    return Amanchik_team_rate;
}

int main() {
    int i, n;
    int scores[200020];
    cin >> n;
    for (int i = 0; i < 2 * n; i++)
        cin >> scores[i];
    sort(scores + 1, scores + 2 * n);
    cout << find_highest(scores, 2 * n, scores[0]) << " " << find_lowest(scores, 2 * n, scores[0]);
    return 0;
}