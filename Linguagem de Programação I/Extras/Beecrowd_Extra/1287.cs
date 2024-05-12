using System;

class Program
{
    static void Main()
    {
        string s;
        while ((s = Console.ReadLine()) != null)
        {
            for (int i = 0; i < s.Length; ++i)
            {
                if (s[i] == 'O' || s[i] == 'o')
                {
                    s = s.Remove(i, 1).Insert(i, "0");
                }
                else if (s[i] == 'l')
                {
                    s = s.Remove(i, 1).Insert(i, "1");
                }
                else if (s[i] == ',' || s[i] == ' ')
                {
                    s = s.Remove(i, 1);
                    --i;
                }
            }

            if (!long.TryParse(s, out long num) || num > 2147483647 || s == "")
            {
                Console.WriteLine("error");
            }
            else
            {
                Console.WriteLine(num);
            }
        }
    }
}