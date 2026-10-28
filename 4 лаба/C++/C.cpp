#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> he;

void prosVVERH() {
    int i = he.size() - 1;
    while (i > 0 && he[i] < he[(i - 1) / 2]) {
        swap(he[i], he[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

void prosVNIS() {
    int n = he.size();
    int i = 0;
    while (true) {
        int maxx = i;
        if (2*i+1 < n && he[2*i+1] < he[maxx]) maxx = 2*i+1;
        if (2*i+2 < n && he[2*i+2] < he[maxx]) maxx = 2*i+2;
        if (maxx == i) break;
        swap(he[i], he[maxx]);
        i = maxx;
    }
}

void insert(int k) {
    he.push_back(k);
    prosVVERH();
}

int extract() {
    if (he.empty()) return -1;
    int res = he[0];
    he[0] = he.back();
    he.pop_back();
    if (!he.empty()) prosVNIS();
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    string comm;
    while (cin >> comm) {
        if (comm == "CLEAR") {
            he.clear();
        } else if (comm == "ADD") {
            int x;
            cin >> x;
            insert(x);
        } else if (comm == "EXTRACT") {
            if (he.empty()) {
                cout << "CANNOT\n";
            } else {
                cout << extract() << "\n";
            }
        }
    }

    return 0;
}
