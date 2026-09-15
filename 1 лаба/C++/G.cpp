#include <iostream>
#include <vector>
using namespace std;

void CountSort(vector<int> &arr) {
  int count[101] = {0};

  for (int i = 0; i < (int)arr.size(); i++) {
    count[arr[i]]++;
  }

  int idx = 0;
  for (int i = 0; i <= 100; i++) {
    while (count[i] > 0) {
      arr[idx] = i;
      idx++;
      count[i]--;
    }
  }
}

int main() {
  vector<int> arr;
  int x;
  while (cin >> x) {
    arr.push_back(x);
  }

  CountSort(arr);

  for (int i = 0; i < (int)arr.size(); i++) {
    cout << arr[i];
    if (i + 1 < (int)arr.size()) {
      cout << " ";
    }
  }
  cout << endl;

  return 0;
}
