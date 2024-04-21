import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            int L = scanner.nextInt();
            int C = scanner.nextInt();
            int R1 = scanner.nextInt();
            int R2 = scanner.nextInt();
            if (L == 0 && C == 0 && R1 == 0 && R2 == 0)
                break;

            if (2 * Math.max(R1, R2) > Math.min(L, C)) {
                System.out.println("N");
                continue;
            }

            if (Math.pow(R1 + R2, 2) <= Math.pow(L - R1 - R2, 2) + Math.pow(C - R1 - R2, 2))
                System.out.println("S");
            else
                System.out.println("N");
        }
        scanner.close();
    }
}