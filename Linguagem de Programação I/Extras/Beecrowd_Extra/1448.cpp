#include <iostream>
#include <string>

int main() {
    int t;
    std::cin >> t;
    std::cin.ignore(); 
    for (int i = 1; i <= t; i++) {
        std::string correct, team1, team2;
        std::getline(std::cin, correct);
        std::getline(std::cin, team1);
        std::getline(std::cin, team2);

        int score1 = 0, score2 = 0;
        for (int j = 0; j < correct.size(); j++) {
            if (correct[j] == team1[j]) {
                score1++;
            }
            if (correct[j] == team2[j]) {
                score2++;
            }
        }

        std::cout << "Instancia " << i << std::endl;
        if (score1 > score2) {
            std::cout << "time 1" << std::endl;
        } else if (score1 < score2) {
            std::cout << "time 2" << std::endl;
        } else {
            bool tieBreaker = false;
            for (int j = 0; j < correct.size(); j++) {
                if (correct[j] == team1[j] && correct[j] != team2[j]) {
                    std::cout << "time 1" << std::endl;
                    tieBreaker = true;
                    break;
                } else if (correct[j] != team1[j] && correct[j] == team2[j]) {
                    std::cout << "time 2" << std::endl;
                    tieBreaker = true;
                    break;
                }
            }
            if (!tieBreaker) {
                std::cout << "empate" << std::endl;
            }
        }
        std::cout << std::endl;
    }
    return 0;
}