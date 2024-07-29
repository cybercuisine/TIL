from collections import deque


def MI():
    return map(int, input().split())


N, K = MI()
A = list(MI())

def count_ways_up_to_x(x):
    dp = set()
    queue = deque([0])
    while queue:
        current = queue.popleft()
        if current > x:
            continue
        if current not in dp:
            if current != 0:
                dp.add(current)
            if len(dp) >= K:
                return K
            for a in A:
                if current + a <= x:
                    queue.append(current + a)
    return len(dp)

A.sort()

left = 1
right = 10**15

while right - 1 > left:
    mid = (left + right) // 2
    if count_ways_up_to_x(mid) >= K:
        right = mid
    else:
        left = mid


print(right)

"""
// TLE in PyPy, submitted below.

#include <iostream>
#include <vector>
#include <deque>
#include <set>
#include <algorithm>
#include <sstream>

using namespace std;

vector<int> read_ints() {
    string line;
    getline(cin, line);
    istringstream iss(line);
    vector<int> result;
    int number;
    while (iss >> number) {
        result.push_back(number);
    }
    return result;
}

int count_ways_up_to_x(int x, const vector<int>& A, int K) {
    set<int> dp;
    deque<int> queue;
    queue.push_back(0);

    while (!queue.empty()) {
        int current = queue.front();
        queue.pop_front();

        if (current > x) {
            continue;
        }
        if (dp.find(current) == dp.end()) {
            if (current != 0) {
                dp.insert(current);
            }
            if (dp.size() >= K) {
                return K;
            }
            for (int a : A) {
                if (current + a <= x) {
                    queue.push_back(current + a);
                }
            }
        }
    }
    return dp.size();
}

int main() {
    // Read N and K
    vector<int> first_line = read_ints();
    int N = first_line[0];
    int K = first_line[1];

    // Read A
    vector<int> A = read_ints();

    // Sort A
    sort(A.begin(), A.end());

    long long left = 1;
    long long right = 10000000000000000LL; // 10^15

    while (right - 1 > left) {
        long long mid = (left + right) / 2;
        if (count_ways_up_to_x(mid, A, K) >= K) {
            right = mid;
        } else {
            left = mid;
        }
    }

    cout << right << endl;

    return 0;
}

"""