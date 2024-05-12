import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = 1;
        while (true) {
            int N = scanner.nextInt();
            int Q = scanner.nextInt();
            if (N == 0 && Q == 0) break;

            int[] marmores = new int[N];
            for (int i = 0; i < N; ++i) {
                marmores[i] = scanner.nextInt();
            }

            Arrays.sort(marmores);

            System.out.println("CASE# " + T++ + ":");

            for (int i = 0; i < Q; ++i) {
                int consulta = scanner.nextInt();

                int index = Arrays.binarySearch(marmores, consulta);

                if (index < 0)
                    System.out.println(consulta + " not found");
                else {
                    // Arrays.binarySearch might not return the index of the first occurrence.
                    // We need to handle this case.
                    while (index > 0 && marmores[index - 1] == consulta) {
                        index--;
                    }
                    System.out.println(consulta + " found at " + (index + 1));
                }
            }
        }
    }
}