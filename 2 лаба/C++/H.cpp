#include <iostream>
using namespace std;

int main() {
  long long w, h, n;
  cin >> w >> h >> n;

  auto can = [&](long long size) -> bool {
    long long rows = size / h;
    long long cols = size / w;
    return rows * cols >= n;
  };

  long long l = 0;
  long long r = max(w, h) * n;

  while (l + 1 < r) {
    long long mid = (l + r) / 2;
    if (can(mid)) {
      r = mid;
    } else {
      l = mid;
    }
  }
  cout << r << endl;
  return 0;
}
