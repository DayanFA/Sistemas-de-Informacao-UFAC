#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct Pair {
    int key;
    int value;
};

bool compare(const Pair &a, const Pair &b) {
    return a.key < b.key;
}

int main() {
    int T = 0;
    int N;
    while (cin >> N && N != 0) {
        if (T > 0) {
            cout << "\n";
        }

        int totalX = 0, totalY = 0;
        vector<Pair> consumos;
        for (int i = 0; i < N; i++) {
            int X, Y;
            cin >> X >> Y;
            totalX += X;
            totalY += Y;
            int key = Y / X;
            auto it = find_if(consumos.begin(), consumos.end(), [key](const Pair &p) { return p.key == key; });
            if (it != consumos.end()) {
                it->value += X;
            } else {
                consumos.push_back({key, X});
            }
        }

        T += 1;
        cout << "Cidade# " << T << ":\n";

        sort(consumos.begin(), consumos.end(), compare);
        for (const auto &p : consumos) {
            cout << p.value << "-" << p.key << " ";
        }
        cout << "\n";

        double consumo_medio = floor((100.0 * totalY) / totalX) / 100;
        printf("Consumo medio: %.2f m3.\n", consumo_medio);
    }
    return 0;
}