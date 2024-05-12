import java.util.*;
import java.math.*;

public class Main {
    static class Pair {
        int key;
        int value;

        Pair(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = 0;
        while (scanner.hasNextInt()) {
            int N = scanner.nextInt();
            if (N == 0) break;

            if (T > 0) System.out.println();

            int totalX = 0, totalY = 0;
            List<Pair> consumos = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                int X = scanner.nextInt();
                int Y = scanner.nextInt();
                totalX += X;
                totalY += Y;
                int key = Y / X;
                boolean found = false;
                for (Pair pair : consumos) {
                    if (pair.key == key) {
                        pair.value += X;
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    consumos.add(new Pair(key, X));
                }
            }

            T++;
            System.out.println("Cidade# " + T + ":");

            consumos.sort(Comparator.comparingInt(a -> a.key));
            for (Pair pair : consumos) {
                System.out.print(pair.value + "-" + pair.key + " ");
            }
            System.out.println();

            double consumo_medio = Math.floor((100.0 * totalY) / totalX) / 100;
            System.out.printf(Locale.US, "Consumo medio: %.2f m3.\n", consumo_medio);
        }
    }
}