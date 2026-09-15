#include <iostream>
#include <vector>
using namespace std;

void BubbleSort(vector<int> &arr) {
  int n = arr.size();
  for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - 1 - i; j++) {
      if (arr[j] < arr[j + 1]) {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

int main() {
  vector<int> arr;
  int x;
  while (cin >> x) {
    arr.push_back(x);
  }

  BubbleSort(arr);

  for (int i = 0; i < (int)arr.size(); i++) {
    cout << arr[i];
    if (i + 1 < (int)arr.size()) {
      cout << " ";
    }
  }
  cout << endl;

  return 0;
}
