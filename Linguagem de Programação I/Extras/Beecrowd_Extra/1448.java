import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        scanner.nextLine(); 
        for (int i = 1; i <= t; i++) {
            String correct = scanner.nextLine();
            String team1 = scanner.nextLine();
            String team2 = scanner.nextLine();

            int score1 = 0;
            int score2 = 0;
            for (int j = 0; j < correct.length(); j++) {
                if (correct.charAt(j) == team1.charAt(j)) {
                    score1++;
                }
                if (correct.charAt(j) == team2.charAt(j)) {
                    score2++;
                }
            }

            System.out.println("Instancia " + i);
            if (score1 > score2) {
                System.out.println("time 1");
            } else if (score1 < score2) {
                System.out.println("time 2");
            } else {
                boolean tieBreaker = false;
                for (int j = 0; j < correct.length(); j++) {
                    if (correct.charAt(j) == team1.charAt(j) && correct.charAt(j) != team2.charAt(j)) {
                        System.out.println("time 1");
                        tieBreaker = true;
                        break;
                    } else if (correct.charAt(j) != team1.charAt(j) && correct.charAt(j) == team2.charAt(j)) {
                        System.out.println("time 2");
                        tieBreaker = true;
                        break;
                    }
                }
                if (!tieBreaker) {
                    System.out.println("empate");
                }
            }
            System.out.println();
        }
        scanner.close();
    }
}