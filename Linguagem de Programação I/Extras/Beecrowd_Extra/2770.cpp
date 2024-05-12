#include <iostream>

int main() {
    int X, Y, M, Xi, Yi;

    while (std::cin >> X >> Y >> M) {
        for (int i = 0; i < M; ++i) {
            std::cin >> Xi >> Yi;
            if ((Xi <= X && Yi <= Y) || (Xi <= Y && Yi <= X)) {
                std::cout << "Sim\n";
            } else {
                std::cout << "Nao\n";
            }
        }
    }

    return 0;
}