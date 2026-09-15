#include <iostream>
#include <vector>

using namespace std;

void InsertionSort(vector<int> &arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    vector<int> arr;
    int x;
    while (cin >> x) {
        arr.push_back(x);
    }

    InsertionSort(arr);

    for (int i = 0; i < (int)arr.size(); i++) {
        cout << arr[i];
        if (i + 1 < (int)arr.size()) {
            cout << " ";
        }
    }
    cout << endl;

    return 0;
}
