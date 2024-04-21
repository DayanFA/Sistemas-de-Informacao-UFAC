using System;
using System.Collections.Generic;

class Program
{
    static bool IsPrime(int n)
    {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int p = 3; p * p <= n; p += 2)
        {
            if (n % p == 0) return false;
        }
        return true;
    }

    static void Main(string[] args)
    {
        int M, N;
        while (int.TryParse(Console.ReadLine(), out M))
        {
            List<int> coins = new List<int>();
            for (int i = 0; i < M; i++)
            {
                coins.Add(int.Parse(Console.ReadLine()));
            }
            N = int.Parse(Console.ReadLine());
            int sumCoins = 0;
            for (int i = M - 1; i >= 0; i -= N)
            {
                sumCoins += coins[i];
            }
            if (IsPrime(sumCoins))
            {
                Console.WriteLine("You’re a coastal aircraft, Robbie, a large silver aircraft.");
            }
            else
            {
                Console.WriteLine("Bad boy! I’ll hit you.");
            }
        }
    }
}