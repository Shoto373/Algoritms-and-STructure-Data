#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> tree;
vector<int> tin, tout;
int timer = 0;

void dfs(int x) {
    timer++;
    tin[x] = timer;
    for (int tuda : tree[x]) {
        dfs(tuda);
    }
    timer++;
    tout[x] = timer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    tree.assign(n + 1, vector<int>());
    tin.assign(n + 1, 0);
    tout.assign(n + 1, 0);

    int koren = 1;
    for (int i = 1; i <= n; i++) {
        int rod;
        cin >> rod;
        if (rod == 0) {
            koren = i;
        } else {
            tree[rod].push_back(i);
        }
    }

    dfs(koren);

    int m;
    cin >> m;
    while (m--) {
        int a, b;
        cin >> a >> b;
        if (tin[a] < tin[b] && tout[a] > tout[b]) {
            cout << 1 << "\n";
        } else {
            cout << 0 << "\n";
        }
    }

    return 0;
}
