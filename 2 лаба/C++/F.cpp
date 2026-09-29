#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    long long N, x, y;
    cin >> N >> x >> y;

    long long l = -1;
    long long r = (N - 1) * max(x, y);

    while (l + 1 < r) {
        long long mid = (l + r) / 2;
        if ((mid / x) + (mid / y) >= N - 1) {
            r = mid;
        } else {
            l = mid;
        }
    }
    cout << r + min(x, y) << endl;
    return 0;
}
