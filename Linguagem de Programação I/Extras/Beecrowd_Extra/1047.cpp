#include <iostream>

int main() {
    int sh, sm, eh, em;
    std::cin >> sh >> sm >> eh >> em;
    int st = sh * 60 + sm;
    int et = eh * 60 + em;
    int d = et - st;
    if (d <= 0) {
        d += 24 * 60;
    }
    int h = d / 60;
    int m = d % 60;
    std::cout << "O JOGO DUROU " << h << " HORA(S) E " << m << " MINUTO(S)\n";
    return 0;
}