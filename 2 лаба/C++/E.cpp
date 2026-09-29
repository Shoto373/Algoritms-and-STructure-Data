#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    auto can = [&](long long d) -> bool {
        int CountzanStoyl = 1;
        int lastStoyl = a[0];

        for (int pos : a) {
            if (lastStoyl + d > pos) {
                continue;
            } else {
                CountzanStoyl++;
                lastStoyl = pos;
            }
        }
        return CountzanStoyl >= K;
    };

    long long l = 0;
    long long r = a[N - 1] - a[0] + 1;

    while (l + 1 < r) {
        long long mid = (l + r) / 2;
        if (can(mid)) {
            l = mid;
        } else {
            r = mid;
        }
    }
    cout << l << endl;
    return 0;
}
