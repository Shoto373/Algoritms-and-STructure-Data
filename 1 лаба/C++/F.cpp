#include <iostream>
#include <vector>
using namespace std;

void quick_sort(vector<int> &arr, int left, int right) {
  if (left >= right) return;
  int pivot = arr[left + (right - left) / 2];
  int i = left, j = right;
  while (i <= j) {
    while (arr[i] < pivot) i++;
    while (arr[j] > pivot) j--;
    if (i <= j) {
      swap(arr[i], arr[j]);
      i++;
      j--;
    }
  }
  if (left < j) quick_sort(arr, left, j);
  if (i < right) quick_sort(arr, i, right);
}

int main() {
  int n;
  if (!(cin >> n)) return 0;
  vector<int> arr(n);
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  quick_sort(arr, 0, n - 1);
  for (int i = 0; i < n; i++) {
    cout << arr[i] << (i + 1 < n ? " " : "\n");
  }
  return 0;
}
