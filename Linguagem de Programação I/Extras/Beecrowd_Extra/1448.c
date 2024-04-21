#include <stdio.h>
#include <string.h>

int main() {
    int t;
    scanf("%d", &t);
    getchar(); 
    for (int i = 1; i <= t; i++) {
        char correct[1000], team1[1000], team2[1000];
        fgets(correct, sizeof(correct), stdin);
        fgets(team1, sizeof(team1), stdin);
        fgets(team2, sizeof(team2), stdin);

        correct[strlen(correct) - 1] = '\0'; 
        team1[strlen(team1) - 1] = '\0'; 
        team2[strlen(team2) - 1] = '\0';

        int score1 = 0, score2 = 0;
        for (int j = 0; j < strlen(correct); j++) {
            if (correct[j] == team1[j]) {
                score1++;
            }
            if (correct[j] == team2[j]) {
                score2++;
            }
        }

        printf("Instancia %d\n", i);
        if (score1 > score2) {
            printf("time 1\n");
        } else if (score1 < score2) {
            printf("time 2\n");
        } else {
            int tieBreaker = 0;
            for (int j = 0; j < strlen(correct); j++) {
                if (correct[j] == team1[j] && correct[j] != team2[j]) {
                    printf("time 1\n");
                    tieBreaker = 1;
                    break;
                } else if (correct[j] != team1[j] && correct[j] == team2[j]) {
                    printf("time 2\n");
                    tieBreaker = 1;
                    break;
                }
            }
            if (!tieBreaker) {
                printf("empate\n");
            }
        }
        printf("\n");
    }
    return 0;
}