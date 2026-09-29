#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;

    vector<long long> verevki(N);
    long long maxV = 0, sumV = 0;
    for (int i = 0; i < N; i++) {
        cin >> verevki[i];
        maxV = max(maxV, verevki[i]);
        sumV += verevki[i];
    }

    auto can = [&](long long ln) -> bool {
        int countVer = 0;
        if (ln * K <= sumV) {
            for (long long x : verevki) {
                if (x < ln) {
                    continue;
                } else {
                    countVer += x / ln;
                }
            }
        }
        return countVer >= K;
    };

    long long l = 0;
    long long r = (long long)N * maxV;

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
