using System;

class Program {
    static void Main() {
        string[] inputs = Console.ReadLine().Split(' ');
        int a = int.Parse(inputs[0]);
        int b = int.Parse(inputs[1]);

        int q = a / b;
        int r = a % b;

        if (r < 0) {
            r += Math.Abs(b);
            q = (a - r) / b;
        }

        Console.WriteLine($"{q} {r}");
    }
}