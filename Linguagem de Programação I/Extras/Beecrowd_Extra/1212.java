import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNext()) {
            String a = scanner.next();
            String b = scanner.next();
            int carry = 0;
            int c = 0;
            if (a.equals("0") && b.equals("0")) {
                break;
            }

            while (a.length() < b.length()) {
                a = "0" + a;
            }
            while (b.length() < a.length()) {
                b = "0" + b;
            }

            for (int i = a.length() - 1; i >= 0; i--) {
                if ((Character.getNumericValue(a.charAt(i)) + Character.getNumericValue(b.charAt(i)) > 9) ||
                    (Character.getNumericValue(a.charAt(i)) + Character.getNumericValue(b.charAt(i)) + c > 9)) {
                    carry += 1;
                    c = 1;
                } else {
                    c = 0;
                }
            }

            if (carry == 0) {
                System.out.println("No carry operation.");
            } else if (carry == 1) {
                System.out.println("1 carry operation.");
            } else {
                System.out.println(carry + " carry operations.");
            }
        }

        scanner.close();
    }
}