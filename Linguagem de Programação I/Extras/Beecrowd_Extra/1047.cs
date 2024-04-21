using System;

class Program
{
    static void Main()
    {
        string[] inputs = Console.ReadLine().Split(' ');
        int sh = int.Parse(inputs[0]);
        int sm = int.Parse(inputs[1]);
        int eh = int.Parse(inputs[2]);
        int em = int.Parse(inputs[3]);

        int st = sh * 60 + sm;
        int et = eh * 60 + em;
        int d = et - st;
        if (d <= 0)
        {
            d += 24 * 60;
        }
        int h = d / 60;
        int m = d % 60;
        Console.WriteLine($"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)");
    }
}