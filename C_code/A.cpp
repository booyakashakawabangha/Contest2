# include <iostream>
using namespace std;

int main() {
    int n = 3;
    int flag;
    int array[500];
    int array2[1000];
    while (true) {
        cin >> flag;
        if (flag == 1) break;

        for (int i = 0; i < n; i++) {
            cin >> array[i] >> array2[i];
        }

        for (int i = 0; i < n; i++) {
            cout << array[i] << " " << array2[i] << endl;
        }
    }
    

    return 0;
}