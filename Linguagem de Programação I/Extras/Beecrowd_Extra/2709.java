import java.util.Scanner;

public class Main {
    public static boolean is_prime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        int p = 3;
        while (p * p <= n) {
            if (n % p == 0) {
                return false;
            }
            p += 2;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            int M = scanner.nextInt();
            int[] coins = new int[M];
            for (int i = 0; i < M; i++) {
                coins[i] = scanner.nextInt();
            }
            int N = scanner.nextInt();
            int sum_coins = 0;
            for (int i = M - 1; i >= 0; i -= N) {
                sum_coins += coins[i];
            }
            if (is_prime(sum_coins)) {
                System.out.println("You’re a coastal aircraft, Robbie, a large silver aircraft.");
            } else {
                System.out.println("Bad boy! I’ll hit you.");
            }
        }
    }
}