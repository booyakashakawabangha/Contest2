# include <iostream>
# include <bits/stdc++.h>
# include <vector>
using namespace std;

int find_highest(vector<int> rates, int nteams) {
    int Amanchik_team_score = rates[0];
    rates.erase(rates.begin());
    sort(rates.begin(), rates.end());
    Amanchik_team_score += rates.back();
    rates.pop_back();
    int Amanchik_team_rate = 1;
    while (rates.size() > 0) {
        int current_rate = rates[0];
        rates.erase(rates.begin());
        int gap = Amanchik_team_score - current_rate;
        int idx = rates.size() - 1;
        
        while (rates[idx] > gap && idx >= 0) idx--;
        current_rate += rates[idx];
        rates.erase(rates.begin() + idx);
        if (current_rate > Amanchik_team_score) {
            Amanchik_team_rate++;
        }
    }
    return Amanchik_team_rate;
}

int find_lowest(vector<int> rates, int nteams) {
    int Amanchik_team_score = rates[0];
    rates.erase(rates.begin());
    sort(rates.begin(), rates.end());
    Amanchik_team_score += rates.front();
    rates.erase(rates.begin());
    int Amanchik_team_rate = nteams;
    while (rates.size() > 0) {
        int current_rate = rates.back();
        rates.pop_back();
        int gap = Amanchik_team_score - current_rate;
        int idx = rates.size() - 1;
        while (rates[idx] > gap && idx >= 0) idx--;
        current_rate += rates[idx];
        rates.erase(rates.begin() + idx);
        if (current_rate <= Amanchik_team_score) {
            Amanchik_team_rate--;
        }
    }
    return Amanchik_team_rate;
}

int main() {
    int n;
    cin >> n;
    // int n = 3;
    // vector<int> rankings = {1, 1, 1, 1, 1, 1};
    vector <int> rankings(2 * n);
    for(int idx = 0; idx < n; idx++) {
        cin >> rankings[idx];
    }
    cout << find_highest(rankings, n) << " " << find_lowest(rankings, n);
}