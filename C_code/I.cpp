# include <iostream>
using namespace std;


int main() {
    int n;
    int money_axis;
    float cash;
    int types[5005];
    float prices[5005];
    
    while (true) {
        cin >> n >> cash;    
        if(n == 0 && cash == 0.00)
            break;

        for (int i = 0; i < n; i++) {
            cin >> types[i] >> prices[i];
        }

        money_axis = 100 * (int) cash;
        int dynamic[n][money_axis];
        int i = n - 1;
        int j = money_axis - 1;
        while (i > 0) {

            while (j > 0) {
                
            }
        }

        
    }
    return 0;
}