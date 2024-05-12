using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int T = 1;
        while (true)
        {
            var input = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            int N = input[0], Q = input[1];
            if (N == 0 && Q == 0) break;

            var marmores = new int[N];
            for (int i = 0; i < N; ++i)
            {
                marmores[i] = int.Parse(Console.ReadLine());
            }

            Array.Sort(marmores);

            Console.WriteLine($"CASE# {T++}:");

            for (int i = 0; i < Q; ++i)
            {
                int consulta = int.Parse(Console.ReadLine());

                int index = Array.IndexOf(marmores, consulta);

                if (index < 0)
                    Console.WriteLine($"{consulta} not found");
                else
                    Console.WriteLine($"{consulta} found at {index + 1}");
            }
        }
    }
}