#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

struct Point {
  long long x;
  long long y;
  long long dist;
};

bool comparePoints(const Point &a, const Point &b) {
  return a.dist < b.dist;
}

int main() {
  int n;
  if (!(cin >> n)) return 0;
  vector<Point> points(n);
  for (int i = 0; i < n; i++) {
    cin >> points[i].x >> points[i].y;
    points[i].dist = points[i].x * points[i].x + points[i].y * points[i].y;
  }
  sort(points.begin(), points.end(), comparePoints);
  for (int i = 0; i < n; i++) {
    cout << points[i].x << " " << points[i].y << "\n";
  }
  return 0;
}
