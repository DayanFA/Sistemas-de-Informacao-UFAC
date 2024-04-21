using System;

public class Program
{
    public static void Main()
    {
        int t = int.Parse(Console.ReadLine());
        for (int i = 1; i <= t; i++)
        {
            string correct = Console.ReadLine();
            string team1 = Console.ReadLine();
            string team2 = Console.ReadLine();

            int score1 = 0;
            int score2 = 0;
            for (int j = 0; j < correct.Length; j++)
            {
                if (correct[j] == team1[j])
                {
                    score1++;
                }
                if (correct[j] == team2[j])
                {
                    score2++;
                }
            }

            Console.WriteLine("Instancia " + i);
            if (score1 > score2)
            {
                Console.WriteLine("time 1");
            }
            else if (score1 < score2)
            {
                Console.WriteLine("time 2");
            }
            else
            {
                bool tieBreaker = false;
                for (int j = 0; j < correct.Length; j++)
                {
                    if (correct[j] == team1[j] && correct[j] != team2[j])
                    {
                        Console.WriteLine("time 1");
                        tieBreaker = true;
                        break;
                    }
                    else if (correct[j] != team1[j] && correct[j] == team2[j])
                    {
                        Console.WriteLine("time 2");
                        tieBreaker = true;
                        break;
                    }
                }
                if (!tieBreaker)
                {
                    Console.WriteLine("empate");
                }
            }
            Console.WriteLine();
        }
    }
}