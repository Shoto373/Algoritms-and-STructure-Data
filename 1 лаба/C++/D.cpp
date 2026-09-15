#include <iostream>
#include <vector>
using namespace std;

int BubbleSort(vector<int> &arr) {
  int n = arr.size();
  int count = 0;

  for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        count++;
      }
    }
  }

  return count;
}

int main() {
  int n;
  cin >> n;

  vector<int> arr(n);
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  cout << BubbleSort(arr) << endl;

  return 0;
}
