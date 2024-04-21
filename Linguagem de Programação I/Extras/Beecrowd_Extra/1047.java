import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sh = scanner.nextInt();
        int sm = scanner.nextInt();
        int eh = scanner.nextInt();
        int em = scanner.nextInt();
        int st = sh * 60 + sm;
        int et = eh * 60 + em;
        int d = et - st;
        if (d <= 0) {
            d += 24 * 60;
        }
        int h = d / 60;
        int m = d % 60;
        System.out.printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", h, m);
    }
}