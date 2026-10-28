#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, W;
    cin >> n >> W;

    vector<tuple<int,int,int>> arr(n);
    for (int i = 0; i < n; i++) {
        int a, w;
        cin >> a >> w;
        arr[i] = {a, a + w - 1, i + 1};
    }

    sort(arr.begin(), arr.end());

    vector<int> gr(n, 0);
    int cnt = 0;

    // куча хранит (правый конец, номер группы)
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> heapp;

    for (int i = 0; i < n; i++) {
        auto [l, r, num] = arr[i];

        int g;
        if (!heapp.empty() && heapp.top().first < l) {
            g = heapp.top().second;
            heapp.pop();
        } else {
            g = ++cnt;
        }
        gr[i] = g;
        heapp.push({r, g});
    }

    // сортируем индексы по номеру группы
    vector<int> order(n);
    iota(order.begin(), order.end(), 0);
    stable_sort(order.begin(), order.end(), [&](int a, int b) {
        return gr[a] < gr[b];
    });

    cout << cnt << '\n';
    for (int i = 0; i < n; i++) {
        cout << get<2>(arr[order[i]]);
        if (i + 1 < n) cout << ' ';
    }
    cout << '\n';

    return 0;
}

