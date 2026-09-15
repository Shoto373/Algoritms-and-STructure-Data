#include <iostream>
#include <vector>
using namespace std;

void SelectionSort(vector<int> &arr) {
  int n = arr.size();

  for (int i = 0; i < n - 1; i++) {
    int maxi = i;

    for (int j = i + 1; j < n; j++) {
      if (arr[j] > arr[maxi]) {
        maxi = j;
      }
    }

    int temp = arr[i];
    arr[i] = arr[maxi];
    arr[maxi] = temp;
  }
}

int main() {
  vector<int> arr;
  int x;

  while (cin >> x) {
    arr.push_back(x);
  }

  SelectionSort(arr);

  for (int i = 0; i < (int)arr.size(); i++) {
    cout << arr[i];
    if (i + 1 < (int)arr.size()) {
      cout << " ";
    }
  }
  cout << endl;

  return 0;
}
