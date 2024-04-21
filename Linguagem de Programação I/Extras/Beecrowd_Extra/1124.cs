using System;

class Program
{
    static void Main(string[] args)
    {
        while (true)
        {
            string input = Console.ReadLine();
            if (string.IsNullOrEmpty(input))
            {
                break;
            }

            string[] inputs = input.Split(' ');
            int L = int.Parse(inputs[0]);
            int C = int.Parse(inputs[1]);
            int R1 = int.Parse(inputs[2]);
            int R2 = int.Parse(inputs[3]);

            if (L == 0 && C == 0 && R1 == 0 && R2 == 0)
            {
                break;
            }

            if (Math.Max(R1, R2) * 2 > Math.Min(L, C))
            {
                Console.WriteLine('N');
                continue;
            }

            if (Math.Pow(R1 + R2, 2) <= Math.Pow(L - R1 - R2, 2) + Math.Pow(C - R1 - R2, 2))
            {
                Console.WriteLine('S');
            }
            else
            {
                Console.WriteLine('N');
            }
        }
    }
}